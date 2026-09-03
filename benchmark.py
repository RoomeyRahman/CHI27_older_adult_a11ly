import sys
import re
import argparse
import statistics
import spacy
import textstat
from tabulate import tabulate


# ============================================================
# TERMINAL COLORS
# ============================================================

GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
RESET = '\033[0m'


# ============================================================
# TARGET / VERDICT HELPERS
# ============================================================

def get_verdict_label(is_pass):
    """Return a color-formatted Pass/Fail label."""
    if is_pass:
        return f"{GREEN}{BOLD}Pass{RESET}"
    return f"{RED}{BOLD}Fail{RESET}"


def check_target(score, t_type="range", t_min=None, t_max=None):
    """
    Evaluate whether a score meets the target.

    score:
        Numeric value or None.

    t_type:
        "range" -> t_min <= score <= t_max
        "max"   -> score <= t_max
        "min"   -> score >= t_min
        "exact" -> score == t_min
    """

    if score is None:
        return f"{YELLOW}{BOLD}N/A{RESET}"

    try:
        if t_type == "range":
            return get_verdict_label(t_min <= score <= t_max)

        elif t_type == "max":
            return get_verdict_label(score <= t_max)

        elif t_type == "min":
            return get_verdict_label(score >= t_min)

        elif t_type == "exact":
            return get_verdict_label(score == t_min)

    except (TypeError, ValueError):
        pass

    return get_verdict_label(False)


def make_result_row(
    name,
    score,
    target,
    t_type,
    t_min=None,
    t_max=None,
    decimals=2
):
    """
    Build one result row.

    Verdict is calculated using the same rounded value displayed
    to the user, avoiding cases such as:

        Score displayed: 21.00
        Actual score:    21.004
        Verdict:         Fail
    """

    if score is None:
        display_score = "N/A"
        verdict_score = None

    elif isinstance(score, int):
        display_score = score
        verdict_score = score

    else:
        display_score = round(score, decimals)
        verdict_score = display_score

    verdict = check_target(
        verdict_score,
        t_type=t_type,
        t_min=t_min,
        t_max=t_max
    )

    return [
        name,
        display_score,
        target,
        verdict
    ]


# ============================================================
# TEXT PREPROCESSING
# ============================================================

def remove_reference_section(text):
    """
    Remove the References/Bibliography section and everything after it.

    This prevents reference entries from distorting:
        - readability
        - sentence length
        - vocabulary diversity
        - citation density
        - first-person frequency
        - connective frequency
        - etc.

    Assumes REFERENCES / References / Bibliography appears on its own line.
    """

    pattern = re.compile(
        r'(?im)^\s*(?:references|bibliography)\s*$'
    )

    match = pattern.search(text)

    if match:
        return text[:match.start()].rstrip()

    return text


def remove_quoted_content(text):
    """
    Remove text inside double quotation marks.

    Useful for qualitative CHI papers because participant quotations
    should not strongly influence measurements of AUTHOR prose.

    Handles:
        "straight quotes"
        “curly quotes”

    This is intentionally optional because some users may want to
    benchmark the complete manuscript.
    """

    # Curly double quotation marks
    text = re.sub(
        r'“.*?”',
        ' ',
        text,
        flags=re.DOTALL
    )

    # Straight double quotation marks
    text = re.sub(
        r'".*?"',
        ' ',
        text,
        flags=re.DOTALL
    )

    # Normalize extra whitespace introduced by quote removal
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n[ \t]+', '\n', text)

    return text


def is_section_heading(line):
    """
    Heuristically determine whether a line is a section heading.

    Recognizes common formats such as:

        # Introduction
        ## Related Work

        1 INTRODUCTION
        2 RELATED WORK
        3.1 Participants
        4.2.1 Analysis

        INTRODUCTION
        RELATED WORK
        METHODS

    This is still heuristic because arbitrary plain-text files do not
    contain machine-readable section information.
    """

    stripped = line.strip()

    if not stripped:
        return False

    # Markdown headings
    if re.match(r'^#{1,6}\s+\S+', stripped):
        return True

    # Numbered headings:
    # 1 INTRODUCTION
    # 2. Related Work
    # 3.1 Participants
    # 4.2.1 Analysis Procedure
    if re.match(
        r'^\d+(?:\.\d+)*\.?\s+[A-Za-z][A-Za-z0-9 ,:&()/\-–—]+$',
        stripped
    ):
        # Avoid treating very long ordinary sentences as headings
        if len(stripped.split()) <= 15:
            return True

    # Roman numeral headings:
    # I. INTRODUCTION
    # IV. METHODS
    if re.match(
        r'^[IVXLCDM]+\.?\s+[A-Za-z][A-Za-z0-9 ,:&()/\-–—]+$',
        stripped
    ):
        if len(stripped.split()) <= 15:
            return True

    # Short ALL-CAPS headings
    # INTRODUCTION
    # RELATED WORK
    if (
        stripped.isupper()
        and len(stripped.split()) <= 10
        and any(c.isalpha() for c in stripped)
    ):
        return True

    return False


def split_into_sections(text):
    """
    Split plain text into sections based on detected section headings.

    Importantly, this does NOT treat every paragraph as a section.

    If no headings are found, the entire document is considered one section.
    """

    lines = text.splitlines()

    sections = []
    current_section = []

    heading_found = False

    for line in lines:

        if is_section_heading(line):

            heading_found = True

            if current_section:
                content = "\n".join(current_section).strip()

                if content:
                    sections.append(content)

            current_section = []

        else:
            current_section.append(line)

    if current_section:
        content = "\n".join(current_section).strip()

        if content:
            sections.append(content)

    if not sections:
        return [text.strip()] if text.strip() else []

    # If heading detection found nothing meaningful, treat entire text as one
    if not heading_found:
        return [text.strip()]

    return sections


def strip_section_headings(text):
    """
    Remove detected section-heading lines from analysis text.

    Headings such as "INTRODUCTION" should not count as sentences or prose.
    """

    cleaned_lines = []

    for line in text.splitlines():

        if not is_section_heading(line):
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


# ============================================================
# NLP / LEXICAL HELPERS
# ============================================================

def calculate_mattr(words, window_size=100):
    """
    Calculate Moving-Average Type-Token Ratio (MATTR).

    MATTR-100 requires at least 100 words.

    Unlike the previous implementation, texts shorter than the window
    do NOT silently return ordinary TTR while being labeled MATTR-100.
    """

    if len(words) < window_size:
        return None

    ttrs = []

    for i in range(len(words) - window_size + 1):

        window = words[i:i + window_size]

        unique_types = len(set(window))

        ttrs.append(
            unique_types / window_size
        )

    if not ttrs:
        return None

    return sum(ttrs) / len(ttrs)


def get_content_words(sent):
    """
    Return a set of content-word lemmas for a sentence.

    Includes:
        nouns
        verbs
        adjectives
        adverbs

    Excludes:
        stopwords
        punctuation
        other grammatical categories
    """

    return {
        token.lemma_.lower()
        for token in sent
        if (
            token.pos_ in {"NOUN", "VERB", "ADJ", "ADV"}
            and not token.is_stop
            and token.is_alpha
        )
    }


def sentence_is_passive(sent):
    """
    Detect whether a sentence contains a passive construction.

    Uses multiple dependency indicators instead of relying only on auxpass.

    Note:
    This remains a syntactic heuristic rather than a perfect linguistic
    passive-voice classifier.
    """

    passive_dependencies = {
        "auxpass",
        "nsubjpass",
        "csubjpass"
    }

    return any(
        token.dep_ in passive_dependencies
        for token in sent
    )


# ============================================================
# PATTERN COUNTING
# ============================================================

def count_regex_patterns(text, patterns):
    """
    Count all occurrences across a collection of regular-expression patterns.
    """

    total = 0

    for pattern in patterns:
        total += len(
            re.findall(
                pattern,
                text,
                flags=re.IGNORECASE
            )
        )

    return total


def count_citation_brackets(text):
    """
    Count citation BRACKET GROUPS rather than individual cited papers.

    Examples counted as ONE citation bracket each:

        [1]
        [3, 8]
        [27, 34, 46]
        [3–8]
        [Smith et al. 2020]
        [Smith 2020; Jones 2021]

    Generic brackets such as:

        [TODO]
        [Figure here]

    are ignored where possible.
    """

    bracket_contents = re.findall(
        r'\[([^\[\]\n]{1,250})\]',
        text
    )

    citation_count = 0

    numeric_pattern = re.compile(
        r'''
        ^\s*
        \d+
        (?:\s*[-–—]\s*\d+)?
        (?:
            \s*,\s*
            \d+
            (?:\s*[-–—]\s*\d+)?
        )*
        \s*$
        ''',
        re.VERBOSE
    )

    year_pattern = re.compile(
        r'\b(?:19|20)\d{2}[a-z]?\b',
        re.IGNORECASE
    )

    for content in bracket_contents:

        content = content.strip()

        # Numeric ACM-style citation
        if numeric_pattern.match(content):
            citation_count += 1
            continue

        # Author-year-style citation:
        # must contain letters AND a plausible publication year
        if (
            re.search(r'[A-Za-z]', content)
            and year_pattern.search(content)
        ):
            citation_count += 1

    return citation_count


# ============================================================
# MAIN ANALYSIS
# ============================================================

def evaluate_chi_benchmark(
    filepath,
    exclude_quotes=True,
    remove_references=True
):

    # --------------------------------------------------------
    # 1. LOAD FILE
    # --------------------------------------------------------

    try:

        with open(filepath, 'r', encoding='utf-8') as f:
            raw_text = f.read()

    except FileNotFoundError:

        print(
            f"{RED}Error: Could not find file: "
            f"{filepath}{RESET}"
        )

        sys.exit(1)

    except UnicodeDecodeError:

        print(
            f"{RED}Error: File could not be decoded as UTF-8.{RESET}"
        )

        sys.exit(1)


    if not raw_text.strip():

        print(
            f"{RED}Error: The input file is empty.{RESET}"
        )

        sys.exit(1)


    # --------------------------------------------------------
    # 2. PREPROCESS MANUSCRIPT
    # --------------------------------------------------------

    manuscript_text = raw_text

    if remove_references:
        manuscript_text = remove_reference_section(
            manuscript_text
        )

    # Citation analysis uses manuscript text BEFORE quote removal.
    # Participant quotes usually do not contain academic citation brackets,
    # while references have already been removed.
    citation_text = strip_section_headings(
        manuscript_text
    )

    style_text = manuscript_text

    if exclude_quotes:
        style_text = remove_quoted_content(
            style_text
        )

    # Determine sections BEFORE removing headings
    sections = split_into_sections(
        style_text
    )

    # Remove headings from main prose calculations
    analysis_text = strip_section_headings(
        style_text
    )

    if not analysis_text.strip():

        print(
            f"{RED}Error: No analyzable prose remained after preprocessing."
            f"{RESET}"
        )

        sys.exit(1)


    # --------------------------------------------------------
    # 3. LOAD SPACY
    # --------------------------------------------------------

    print(
        f"{CYAN}Loading NLP model...{RESET}"
    )

    try:

        nlp = spacy.load(
            "en_core_web_sm"
        )

    except OSError:

        print(
            f"\n{RED}Error: spaCy model 'en_core_web_sm' "
            f"is not installed.{RESET}\n"
        )

        print(
            "Install it with:\n\n"
            "    python -m spacy download en_core_web_sm\n"
        )

        sys.exit(1)


    # Increase maximum document length for long manuscripts
    if len(analysis_text) >= nlp.max_length:
        nlp.max_length = len(analysis_text) + 1000


    # --------------------------------------------------------
    # 4. BASIC NLP UNITS
    # --------------------------------------------------------

    doc = nlp(
        analysis_text
    )

    sentences = [
        sent
        for sent in doc.sents
        if any(token.is_alpha for token in sent)
    ]

    words = [
        token.text.lower()
        for token in doc
        if token.is_alpha
    ]

    num_words = len(words)
    num_sents = len(sentences)
    num_sections = max(
        len(sections),
        1
    )


    if num_words == 0 or num_sents == 0:

        print(
            f"{RED}Error: No valid words or sentences were detected."
            f"{RESET}"
        )

        sys.exit(1)


    # --------------------------------------------------------
    # 5. READABILITY
    # --------------------------------------------------------

    flesch_reading = (
        textstat.flesch_reading_ease(
            analysis_text
        )
    )

    flesch_kincaid = (
        textstat.flesch_kincaid_grade(
            analysis_text
        )
    )

    gunning_fog = (
        textstat.gunning_fog(
            analysis_text
        )
    )


    # --------------------------------------------------------
    # 6. SENTENCE LENGTH
    # --------------------------------------------------------

    sentence_lengths = [
        len([
            token
            for token in sent
            if token.is_alpha
        ])
        for sent in sentences
    ]


    mean_sent_len = (
        sum(sentence_lengths)
        / num_sents
    )


    # Population SD is appropriate because we are describing all
    # sentences in the supplied manuscript, rather than estimating
    # a larger population from a sample.
    sent_len_sd = (
        statistics.pstdev(
            sentence_lengths
        )
        if num_sents > 1
        else 0
    )


    # --------------------------------------------------------
    # 7. LONG SENTENCES PER ACTUAL SECTION
    # --------------------------------------------------------

    total_long_sentences = 0

    for section in sections:

        section_clean = strip_section_headings(
            section
        )

        if not section_clean.strip():
            continue

        section_doc = nlp(
            section_clean
        )

        for sent in section_doc.sents:

            length = len([
                token
                for token in sent
                if token.is_alpha
            ])

            if length > 35:
                total_long_sentences += 1


    long_sents_per_section = (
        total_long_sentences
        / num_sections
    )


    # Additional useful descriptive measure
    long_sentence_percentage = (
        total_long_sentences
        / num_sents
    ) * 100


    # --------------------------------------------------------
    # 8. POLYSYLLABIC WORDS
    # --------------------------------------------------------

    # Use textstat for BOTH numerator and denominator.
    # This avoids mixing spaCy tokenization with textstat tokenization.
    poly_words = textstat.polysyllabcount(
        analysis_text
    )

    textstat_word_count = textstat.lexicon_count(
        analysis_text,
        removepunct=True
    )

    poly_percentage = (
        (poly_words / textstat_word_count) * 100
        if textstat_word_count > 0
        else 0
    )


    # --------------------------------------------------------
    # 9. MATTR-100
    # --------------------------------------------------------

    mattr_100 = calculate_mattr(
        words,
        window_size=100
    )


    # --------------------------------------------------------
    # 10. ADJACENT SENTENCE CONTENT-WORD OVERLAP
    # --------------------------------------------------------

    # Calculate within sections so the final sentence of one section is
    # not compared with the first sentence of the next section.

    no_share_count = 0
    adjacency_pairs = 0

    for section in sections:

        section_clean = strip_section_headings(
            section
        )

        if not section_clean.strip():
            continue

        section_doc = nlp(
            section_clean
        )

        section_sentences = [
            sent
            for sent in section_doc.sents
            if any(token.is_alpha for token in sent)
        ]

        for i in range(
            len(section_sentences) - 1
        ):

            set1 = get_content_words(
                section_sentences[i]
            )

            set2 = get_content_words(
                section_sentences[i + 1]
            )

            adjacency_pairs += 1

            if not set1.intersection(set2):
                no_share_count += 1


    no_share_percentage = (
        (no_share_count / adjacency_pairs) * 100
        if adjacency_pairs > 0
        else 0
    )


    # --------------------------------------------------------
    # 11. NORMALIZATION FACTOR
    # --------------------------------------------------------

    per_1k = (
        num_words / 1000
    )


    # --------------------------------------------------------
    # 12. CONTRAST MARKERS
    # --------------------------------------------------------

    # These remain heuristic discourse markers.
    #
    # Phrase-level forms are now handled properly rather than looking
    # only for the standalone word "contrast".

    contrast_patterns = [
        r'\bhowever\b',
        r'\bconversely\b',
        r'\balthough\b',
        r'\byet\b',
        r'\bwhereas\b',
        r'\bwhile\b',
        r'\bnevertheless\b',
        r'\bin contrast\b',
        r'\bby contrast\b',
        r'\bon the other hand\b'
    ]

    contrast_count = count_regex_patterns(
        analysis_text,
        contrast_patterns
    )

    contrast_per_1k = (
        contrast_count / per_1k
    )


    # --------------------------------------------------------
    # 13. SELECTED CONNECTIVE TOKENS
    # --------------------------------------------------------

    # IMPORTANT:
    # This is intentionally labeled "selected connective tokens"
    # rather than claiming that every occurrence is a discourse marker.
    #
    # E.g. "and" may simply connect noun phrases, while "since" can
    # have a temporal rather than causal meaning.

    connective_list = {
        "and",
        "but",
        "or",
        "because",
        "therefore",
        "thus",
        "hence",
        "since",
        "so"
    }

    connective_count = sum(
        1
        for word in words
        if word in connective_list
    )

    connective_per_1k = (
        connective_count / per_1k
    )


    # --------------------------------------------------------
    # 14. CITATION BRACKETS
    # --------------------------------------------------------

    citations = count_citation_brackets(
        citation_text
    )

    # Citation denominator should correspond to manuscript text,
    # not the References section.
    citation_doc = nlp(
        citation_text
    )

    citation_word_count = len([
        token
        for token in citation_doc
        if token.is_alpha
    ])

    citation_per_1k_factor = (
        citation_word_count / 1000
        if citation_word_count > 0
        else 1
    )

    citations_per_1k = (
        citations
        / citation_per_1k_factor
    )


    # --------------------------------------------------------
    # 15. FIRST PERSON
    # --------------------------------------------------------

    first_person_list = {
        "i",
        "we",
        "me",
        "us",
        "my",
        "our",
        "mine",
        "ours"
    }

    first_person_count = sum(
        1
        for word in words
        if word in first_person_list
    )

    first_person_per_1k = (
        first_person_count / per_1k
    )


    # --------------------------------------------------------
    # 16. PASSIVE SENTENCES
    # --------------------------------------------------------

    passive_sents = sum(
        1
        for sent in sentences
        if sentence_is_passive(sent)
    )

    passive_percentage = (
        passive_sents
        / num_sents
    ) * 100


    # --------------------------------------------------------
    # 17. BANNED / OVERUSED CONNECTIVES
    # --------------------------------------------------------

    banned_connectives = {
        "moreover",
        "furthermore",
        "additionally"
    }

    banned_count = sum(
        1
        for word in words
        if word in banned_connectives
    )


    # --------------------------------------------------------
    # 18. HYPE WORDS
    # --------------------------------------------------------

    # Regex is used because spaCy separates hyphenated expressions
    # such as "state-of-the-art" into multiple tokens.

    hype_patterns = [
        r'\bgroundbreaking\b',
        r'\brevolutionary\b',
        r'\bnovel\b',
        r'\bparadigm[-\s]shifting\b',
        r'\bgame[-\s]changing\b',
        r'\bstate[-\s]of[-\s]the[-\s]art\b',
        r'\bcutting[-\s]edge\b'
    ]

    hype_count = count_regex_patterns(
        analysis_text,
        hype_patterns
    )


    # ========================================================
    # 19. COMPILE RESULTS
    # ========================================================

    results = [

        make_result_row(
            "Flesch Reading Ease",
            flesch_reading,
            "20–35",
            "range",
            20,
            35
        ),

        make_result_row(
            "Flesch–Kincaid grade",
            flesch_kincaid,
            "13–16",
            "range",
            13,
            16
        ),

        make_result_row(
            "Gunning Fog",
            gunning_fog,
            "17–19",
            "range",
            17,
            19
        ),

        make_result_row(
            "Mean sentence length",
            mean_sent_len,
            "18–21 words",
            "range",
            18,
            21
        ),

        make_result_row(
            "Sentence-length spread (population SD)",
            sent_len_sd,
            "6–9",
            "range",
            6,
            9
        ),

        make_result_row(
            "Sentences >35 words per section",
            long_sents_per_section,
            "≤ 1",
            "max",
            t_max=1
        ),

        make_result_row(
            "Polysyllabic words (%)",
            poly_percentage,
            "25–30",
            "range",
            25,
            30
        ),

        make_result_row(
            "Vocabulary diversity (MATTR-100)",
            mattr_100,
            "0.75–0.80",
            "range",
            0.75,
            0.80,
            decimals=3
        ),

        make_result_row(
            "Adj. sentences with no shared content lemma (%)",
            no_share_percentage,
            "40–55",
            "range",
            40,
            55
        ),

        make_result_row(
            "Contrast markers (per 1k words)",
            contrast_per_1k,
            "6–8",
            "range",
            6,
            8
        ),

        make_result_row(
            "Selected connective tokens (per 1k words)",
            connective_per_1k,
            "75–90",
            "range",
            75,
            90
        ),

        make_result_row(
            "Citation brackets (per 1k words)",
            citations_per_1k,
            "11–14",
            "range",
            11,
            14
        ),

        make_result_row(
            "First-person mentions (per 1k words)",
            first_person_per_1k,
            "5–8",
            "range",
            5,
            8
        ),

        make_result_row(
            "Sentences containing passive construction (%)",
            passive_percentage,
            "20–28",
            "range",
            20,
            28
        ),

        make_result_row(
            "Moreover / Furthermore / Additionally",
            banned_count,
            "0",
            "exact",
            t_min=0
        ),

        make_result_row(
            "Hype words",
            hype_count,
            "0",
            "exact",
            t_min=0
        )
    ]


    # ========================================================
    # 20. OUTPUT
    # ========================================================

    print(
        "\n"
        + f"{CYAN}{BOLD}"
        + "=" * 78
        + f"{RESET}"
    )

    print(
        f"{CYAN}{BOLD}"
        " CHI PROSE PROFILE RESULTS"
        f"{RESET}"
    )

    print(
        f"{CYAN}{BOLD}"
        + "=" * 78
        + f"{RESET}"
    )


    # Analysis configuration
    print(
        f"\n{BOLD}Analysis configuration:{RESET}"
    )

    print(
        f"  Words analyzed:       {num_words}"
    )

    print(
        f"  Sentences analyzed:   {num_sents}"
    )

    print(
        f"  Sections detected:    {num_sections}"
    )

    print(
        f"  Long sentences >35:   "
        f"{total_long_sentences} "
        f"({long_sentence_percentage:.2f}%)"
    )

    print(
        f"  References excluded:  "
        f"{'Yes' if remove_references else 'No'}"
    )

    print(
        f"  Quoted text excluded: "
        f"{'Yes' if exclude_quotes else 'No'}"
    )


    print("\n")

    print(
        tabulate(
            results,
            headers=[
                "Test",
                "Score",
                "Target",
                "Verdict"
            ],
            tablefmt="github"
        )
    )


    # Extra diagnostic counts
    print(
        f"\n{BOLD}Diagnostic counts:{RESET}"
    )

    print(
        f"  Citation bracket groups:     {citations}"
    )

    print(
        f"  Passive sentences:           "
        f"{passive_sents}/{num_sents}"
    )

    print(
        f"  Adjacent sentence pairs:     {adjacency_pairs}"
    )

    print(
        f"  No-overlap adjacent pairs:   {no_share_count}"
    )

    print(
        f"  Contrast markers:            {contrast_count}"
    )

    print(
        f"  Selected connective tokens:  {connective_count}"
    )

    print(
        f"  First-person mentions:       {first_person_count}"
    )

    print(
        f"  Polysyllabic words:          "
        f"{poly_words}/{textstat_word_count}"
    )

    print(
        f"  Banned connective count:     {banned_count}"
    )

    print(
        f"  Hype-word count:             {hype_count}"
    )


    if mattr_100 is None:

        print(
            f"\n{YELLOW}"
            "Note: MATTR-100 is unavailable because the analyzed "
            "text contains fewer than 100 words."
            f"{RESET}"
        )


    print(
        f"\n{YELLOW}"
        "Important: These target ranges are reference/empirical "
        "benchmarks, not official ACM CHI acceptance criteria."
        f"{RESET}"
    )

    print()


# ============================================================
# COMMAND-LINE INTERFACE
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Analyze academic prose using a set of "
            "CHI-oriented reference metrics."
        )
    )

    parser.add_argument(
        "filepath",
        help="Path to the UTF-8 plain-text manuscript."
    )

    parser.add_argument(
        "--include-quotes",
        action="store_true",
        help=(
            "Include quoted material in style metrics. "
            "By default, quoted text is excluded so participant "
            "quotes do not distort author-prose measurements."
        )
    )

    parser.add_argument(
        "--keep-references",
        action="store_true",
        help=(
            "Do not remove the References/Bibliography section. "
            "Normally references should be excluded."
        )
    )

    args = parser.parse_args()

    evaluate_chi_benchmark(
        filepath=args.filepath,

        # Default = remove quoted material
        exclude_quotes=not args.include_quotes,

        # Default = remove references
        remove_references=not args.keep_references
    )


if __name__ == "__main__":
    main()