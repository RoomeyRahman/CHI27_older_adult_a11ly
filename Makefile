# Compile the CHI paper LaTeX project inside the texlive Docker container.
# Usage: make pdf                       (uses default PROJECT)
#        make pdf PROJECT=other_folder  (compile a different project under output/latex/)

PROJECT     ?= CHI27_older_adult_accessibility
MAIN        ?= main
PROPOSAL	?= proposal
PROJECT_DIR := output/latex/$(PROJECT)
BIB_SRC     := references/reference.bib
BIB_DST     := $(PROJECT_DIR)/reference.bib
COMPOSE_FILE := /Users/roomeyrahman/Documents/configurations/docker-compose.yml
# docker-compose.override.yml remaps the shared latex service's volume to
# this repo's output/latex/ (the shared file points at a different project).
OVERRIDE_FILE := docker-compose.override.yml
COMPOSE     := docker compose -f $(COMPOSE_FILE) -f $(OVERRIDE_FILE)

.PHONY: pull pdf pdf-proposal bibtex sync-bib clean cleanall shell logs

# Copy the canonical bibliography into the LaTeX project whenever it's
# missing or stale; main.tex's \bibliography{reference} needs it in place.
sync-bib:
	@if [ ! -f "$(BIB_DST)" ] || ! cmp -s "$(BIB_SRC)" "$(BIB_DST)"; then \
		cp "$(BIB_SRC)" "$(BIB_DST)" && echo "Synced $(BIB_SRC) -> $(BIB_DST)"; \
	fi

# Pull/update the texlive image.
pull:
	$(COMPOSE) pull

# Full build: latexmk drives pdflatex + bibtex/biber reruns as needed.
# -f (force) matches Overleaf behavior: keep going past recoverable LaTeX
# errors (e.g. acmart's titlesec \section-redefinition complaint) and still
# emit the PDF. We then verify the PDF actually exists so real failures
# (missing files, bad syntax) still fail the make target.
pdf: sync-bib
	$(COMPOSE) run --rm latex bash -c "cd $(PROJECT) && (latexmk -pdf -f -interaction=nonstopmode $(MAIN).tex || true) && test -s $(MAIN).pdf && echo 'PDF built: $(PROJECT)/$(MAIN).pdf'"

pdf-proposal: sync-bib
	$(COMPOSE) run --rm latex bash -c "cd $(PROJECT) && (latexmk -pdf -f -interaction=nonstopmode $(PROPOSAL).tex || true) && test -s $(PROPOSAL).pdf && echo 'PDF built: $(PROJECT)/$(PROPOSAL).pdf'"

# Manual pdflatex -> bibtex -> pdflatex -> pdflatex cycle, if latexmk ever misbehaves.
bibtex: sync-bib
	$(COMPOSE) run --rm latex bash -c "cd $(PROJECT) && \
		pdflatex -interaction=nonstopmode $(MAIN).tex && \
		bibtex $(MAIN) && \
		pdflatex -interaction=nonstopmode $(MAIN).tex && \
		pdflatex -interaction=nonstopmode $(MAIN).tex"

# Remove latexmk-generated aux/build artifacts for this project.
clean:
	$(COMPOSE) run --rm latex bash -c "cd $(PROJECT) && latexmk -c $(MAIN).tex"

# Also remove the built PDF.
cleanall:
	$(COMPOSE) run --rm latex bash -c "cd $(PROJECT) && latexmk -C $(MAIN).tex"

# Drop into a shell inside the container, cwd on the project folder.
shell:
	$(COMPOSE) run --rm latex bash -c "cd $(PROJECT) && bash"

# Tail the latexmk log for the last build.
logs:
	$(COMPOSE) run --rm latex bash -c "cd $(PROJECT) && cat $(MAIN).log"
