"""Generate Figure 2: the reward arc running through the family."""

W, H = 1400, 760
INK = "#1b1b1b"
BG = "#FCFBF7"
SW = 3.4

p = []
a = p.append


def text(x, y, s, size=25, weight="400", anchor="middle", style=""):
    a(f'<text x="{x}" y="{y}" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" '
      f'font-size="{size}" font-weight="{weight}" fill="{INK}" text-anchor="{anchor}" '
      f'letter-spacing="{0.6 if weight == "700" else 0}" style="{style}">{s}</text>')


def label(cx, y, s):
    text(cx, y, s, size=25, weight="700")


def phone(x, y, w=92, h=158, tick=False):
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="13" fill="none" stroke="{INK}" stroke-width="{SW}"/>')
    a(f'<rect x="{x+11}" y="{y+20}" width="{w-22}" height="{h-40}" rx="5" fill="none" stroke="{INK}" stroke-width="2.2"/>')
    a(f'<line x1="{x+w/2-13}" y1="{y+11}" x2="{x+w/2+13}" y2="{y+11}" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"/>')
    if tick:
        cx, cy = x + w / 2, y + h / 2
        a(f'<path d="M {cx-16} {cy} l 11 12 l 21 -25" fill="none" stroke="{INK}" stroke-width="3.4" '
          f'stroke-linecap="round" stroke-linejoin="round"/>')


def bubble(x, y, w, h, lines, tail="left", size=23, italic=False):
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{BG}" stroke="{INK}" stroke-width="{SW}"/>')
    if tail == "left":
        a(f'<path d="M {x} {y+h*0.55} l -22 14 l 22 6 z" fill="{BG}" stroke="{INK}" '
          f'stroke-width="{SW}" stroke-linejoin="round"/>')
        a(f'<line x1="{x-1}" y1="{y+h*0.56}" x2="{x-1}" y2="{y+h*0.72}" stroke="{BG}" stroke-width="4"/>')
    elif tail == "bottom":
        a(f'<path d="M {x+w*0.15} {y+h} l 6 24 l 26 -24 z" fill="{BG}" stroke="{INK}" '
          f'stroke-width="{SW}" stroke-linejoin="round"/>')
        a(f'<line x1="{x+w*0.16}" y1="{y+h-1}" x2="{x+w*0.15+26}" y2="{y+h-1}" stroke="{BG}" stroke-width="4"/>')
    sty = "font-style:italic" if italic else ""
    ly = y + h / 2 - (len(lines) - 1) * (size + 7) / 2 + size * 0.34
    for ln in lines:
        text(x + w / 2, ly, ln, size=size, style=sty)
        ly += size + 7


def person(cx, base, scale=1.0, arm=None):
    r = 34 * scale
    hy = base - 108 * scale
    a(f'<circle cx="{cx}" cy="{hy}" r="{r}" fill="none" stroke="{INK}" stroke-width="{SW}"/>')
    a(f'<circle cx="{cx-11*scale}" cy="{hy-4*scale}" r="{3.4*scale}" fill="{INK}"/>')
    a(f'<circle cx="{cx+11*scale}" cy="{hy-4*scale}" r="{3.4*scale}" fill="{INK}"/>')
    a(f'<path d="M {cx-12*scale} {hy+13*scale} q {12*scale} {10*scale} {24*scale} 0" fill="none" '
      f'stroke="{INK}" stroke-width="2.6" stroke-linecap="round"/>')
    a(f'<path d="M {cx-52*scale} {base} q 0 {-58*scale} {52*scale} {-58*scale} q {52*scale} 0 {52*scale} {58*scale}" '
      f'fill="none" stroke="{INK}" stroke-width="{SW}" stroke-linecap="round"/>')
    if arm == "right":
        a(f'<path d="M {cx+40*scale} {base-46*scale} q {34*scale} {6*scale} {44*scale} {-16*scale}" fill="none" '
          f'stroke="{INK}" stroke-width="{SW}" stroke-linecap="round"/>')
    if arm == "left":
        a(f'<path d="M {cx-40*scale} {base-46*scale} q {-34*scale} {6*scale} {-44*scale} {-16*scale}" fill="none" '
          f'stroke="{INK}" stroke-width="{SW}" stroke-linecap="round"/>')


def heatmap(x, y, cols=7, rows=3, cell=21, gap=6, filled=None):
    filled = filled or set()
    for r in range(rows):
        for c in range(cols):
            cx0, cy0 = x + c * (cell + gap), y + r * (cell + gap)
            f = INK if (r, c) in filled else "none"
            a(f'<rect x="{cx0}" y="{cy0}" width="{cell}" height="{cell}" rx="4" fill="{f}" '
              f'stroke="{INK}" stroke-width="2.2"/>')


def arrow(d, dash=False, width=SW):
    da = ' stroke-dasharray="11 9"' if dash else ''
    a(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{width}" stroke-linecap="round" '
      f'marker-end="url(#ah)"{da}/>')


a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
a(f'<defs><marker id="ah" viewBox="0 0 12 12" refX="9.5" refY="6" markerWidth="7.5" markerHeight="7.5" '
  f'orient="auto-start-reverse"><path d="M 1 1 L 11 6 L 1 11 z" fill="{INK}"/></marker></defs>')
a(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

# ---------------------------------------------------------------- top row
phone(118, 96)
bubble(248, 108, 196, 92, ["Time for your", "medicine"], tail="left")
label(286, 300, "THE AGENT REMINDS")

person(640, 236, scale=1.0, arm="right")
phone(706, 132, w=54, h=92, tick=True)
a(f'<circle cx="578" cy="214" r="10" fill="none" stroke="{INK}" stroke-width="2.8"/>')
a(f'<path d="M 598 206 q -10 4 -12 6" fill="none" stroke="{INK}" stroke-width="{SW}" stroke-linecap="round"/>')
label(650, 300, "THE DOSE IS TAKEN")

heatmap(986, 118, cols=7, rows=3,
        filled={(0, 0), (0, 1), (0, 2), (0, 4), (0, 5), (0, 6),
                (1, 0), (1, 1), (1, 3), (1, 4), (1, 5),
                (2, 1), (2, 2), (2, 3), (2, 5), (2, 6)})
text(1080, 240, "14 day streak", size=23)
label(1080, 300, "STREAK AND HEAT MAP RECORD IT")

arrow("M 464 172 L 556 172")
arrow("M 792 172 L 958 172")

# ------------------------------------------------------- right turn down
arrow("M 1200 172 h 80 q 46 0 46 46 v 302 q 0 46 -46 46 h -74")

# ------------------------------------------------------------- bottom row
person(1148, 664, scale=0.82, arm="left")
phone(1058, 574, w=48, h=82)
label(1124, 726, "A FAMILY MEMBER SEES IT")

person(806, 664, scale=0.82, arm="right")
person(676, 664, scale=0.82)
bubble(636, 420, 300, 94, ["You have kept it up", "all week."], tail="bottom", italic=True)
label(741, 726, "THEY SAY SOMETHING")

text(286, 546, "RELATIONAL", size=27, weight="700")
text(286, 580, "TRIGGER", size=27, weight="700")
text(286, 626, "an occasion for the family", size=23)
text(286, 656, "to say something, not a", size=23)
text(286, 686, "private score to defend", size=23)

arrow("M 1040 636 L 892 636")
arrow("M 618 636 L 430 636")

# --------------------------------------------------- return arc to the agent
arrow("M 178 716 h -62 q -50 0 -50 -50 v -436 q 0 -50 50 -50 h 0")
a(f'<text font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="22" fill="{INK}" '
  f'text-anchor="middle" transform="translate(42,420) rotate(-90)">the routine returns to the household</text>')

# ------------------------------------------------- the allegiance branch
arrow("M 640 314 L 640 336", dash=True)
text(782, 330, "no confirmation", size=21)
a(f'<rect x="380" y="344" width="440" height="60" rx="16" fill="none" stroke="{INK}" '
  f'stroke-width="2.8" stroke-dasharray="11 9"/>')
text(600, 382, "The agent asks before telling the family", size=23)
arrow("M 822 380 q 156 14 218 128", dash=True)
text(1064, 452, "granted", size=21)

a('</svg>')


svg = "\n".join(p)
open("fig2.svg", "w").write(svg)
open("fig2.html", "w").write(
    f'<!doctype html><meta charset="utf-8">'
    f'<style>html,body{{margin:0;padding:0;background:{BG}}}</style>{svg}')
print("ok")
