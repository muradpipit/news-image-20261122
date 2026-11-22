#!/usr/bin/env python3
"""Draw the front page of 'The World in One Day' for 22 November 2026.

Renders a 1024x1024 newspaper front page (entry.png) summarising the
day's world news: a NATO/Poland lead story plus a 3x3 grid of briefs.
Deterministic: fixed fonts, fixed layout, no timestamps, no randomness.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

INK = (18, 18, 18)
PAPER = (250, 247, 238)
RULE = (18, 18, 18)
MUTED = (90, 86, 76)
ACCENT = (140, 28, 28)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_font(draw, text, name, start, max_w, min_size=10):
    """Largest font size (<= start) at which text fits on one line."""
    size = start
    while size > min_size:
        fnt = font(name, size)
        if draw.textlength(text, font=fnt) <= max_w:
            return fnt
        size -= 1
    return font(name, min_size)


def draw_centered(draw, y, text, fnt, fill=INK, x0=0, x1=W):
    w = draw.textlength(text, font=fnt)
    draw.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size + 4


MASTHEAD = "THE WORLD IN ONE DAY"
DATELINE = "SUNDAY, 22 NOVEMBER 2026  \u2022  ONE IMAGE, THE WHOLE WORLD"
FOOTER = "THE WORLD IN ONE DAY \u2014 22 NOVEMBER 2026 \u2022 ALL STORIES FIRST REPORTED TODAY"

LEAD_KICKER = "LEAD  \u2022  NATO \u2014 POLAND"
LEAD_HEADLINE = "NATO VOWS TO DEFEND POLAND"
LEAD_SUB = ("Rutte in Warsaw: the alliance will defend \u201cevery inch\u201d of "
            "Polish territory; Poland invokes Article 4; NATO Council meets Monday.")

GRID = [
    ("MARKETS", "Taiwan stocks crash 17.5% in a week",
     "Chip index sinks 10%, TSMC ADR falls; Bitcoin hits a two-year low."),
    ("TECH", "US and China agree human control of military AI",
     "Pact keeps humans in charge of AI weapons decisions."),
    ("DIPLOMACY", "Trump seeks permanent Iran nuclear accord",
     "President wants a lasting deal to stop Tehran building a bomb."),
    ("MIDEAST", "Herzog taps Eisenkot to form Israeli government",
     "Ex-army chief chosen over Netanyahu to try to build a coalition."),
    ("MIDEAST", "Four nations urge Israel to open Gaza aid",
     "Australia, Canada, Italy and the UK cite floods worsening suffering."),
    ("EUROPE", "France hit by fourth weekend of protests",
     "Cost-of-living demonstrations sweep the country again."),
    ("CLIMATE", "COP31 climate talks run into overtime",
     "Delegates in Turkey struggle to agree a final deal."),
    ("AMERICAS", "US details $12bn in Venezuelan oil revenue",
     "State Dept report traces funds a year after Maduro\u2019s capture."),
    ("AFRICA", "Al-Shabaab claims mass ambush on Somali troops",
     "Militants say hundreds dead in attack on army forces."),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Outer frame.
    d.rectangle([14, 14, W - 15, H - 15], outline=RULE, width=3)
    d.rectangle([20, 20, W - 21, H - 21], outline=RULE, width=1)

    # Masthead.
    y = 34
    f_mast = fit_font(d, MASTHEAD, "DejaVuSerif-Bold.ttf", 64, W - 90)
    y = draw_centered(d, y, MASTHEAD, f_mast)
    f_date = font("DejaVuSans.ttf", 19)
    y = draw_centered(d, y + 2, DATELINE, f_date, fill=MUTED)
    d.line([40, y + 8, W - 40, y + 8], fill=RULE, width=3)
    y += 22

    # Lead story.
    f_kick = font("DejaVuSans-Bold.ttf", 20)
    y = draw_centered(d, y, LEAD_KICKER, f_kick, fill=ACCENT)
    f_lead = fit_font(d, LEAD_HEADLINE, "DejaVuSerif-Bold.ttf", 56, W - 90)
    y = draw_centered(d, y + 4, LEAD_HEADLINE, f_lead)
    f_sub = font("DejaVuSerif.ttf", 22)
    sub_lines = wrap(d, LEAD_SUB, f_sub, W - 130)
    for line in sub_lines:
        y = draw_centered(d, y + 2, line, f_sub)
    d.line([40, y + 12, W - 40, y + 12], fill=RULE, width=2)
    grid_top = y + 26

    # 3x3 grid of briefs.
    margin = 40
    gap = 18
    col_w = (W - 2 * margin - 2 * gap) // 3
    grid_bottom = H - 64
    row_h = (grid_bottom - grid_top) // 3
    f_k = font("DejaVuSans-Bold.ttf", 15)
    f_h = font("DejaVuSerif-Bold.ttf", 22)
    f_b = font("DejaVuSans.ttf", 17)

    for i, (kicker, headline, body) in enumerate(GRID):
        r, c = divmod(i, 3)
        x0 = margin + c * (col_w + gap)
        x1 = x0 + col_w
        y0 = grid_top + r * row_h
        if c:
            d.line([x0 - gap // 2, y0 + 4, x0 - gap // 2,
                    y0 + row_h - 10], fill=(190, 186, 174), width=1)
        if r:
            d.line([x0, y0 - 9, x1, y0 - 9], fill=(190, 186, 174), width=1)
        cy = y0 + 2
        d.text((x0, cy), kicker, font=f_k, fill=ACCENT)
        cy += f_k.size + 8
        for line in wrap(d, headline, f_h, col_w):
            d.text((x0, cy), line, font=f_h, fill=INK)
            cy += f_h.size + 4
        cy += 2
        for line in wrap(d, body, f_b, col_w):
            d.text((x0, cy), line, font=f_b, fill=MUTED)
            cy += f_b.size + 3

    # Footer.
    d.line([40, H - 56, W - 40, H - 56], fill=RULE, width=2)
    f_f = font("DejaVuSans-Bold.ttf", 15)
    draw_centered(d, H - 46, FOOTER, f_f, fill=MUTED)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
