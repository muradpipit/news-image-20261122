[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/muradpipit/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/muradpipit/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# The World in One Day — 22 November 2026

A 1024×1024 newspaper front page summarising the world's news for
Sunday, 22 November 2026 — drawn entirely in code with Python + Pillow.

**Lead story:** NATO vows to defend Poland — Rutte in Warsaw promises the
alliance will defend "every inch" of Polish territory; Poland invokes
Article 4 and the NATO Council meets Monday.

**Nine briefs:** Taiwan stocks crash 17.5% in a week; US and China agree on
human control of military AI; Trump seeks a permanent Iran nuclear accord;
Herzog taps Eisenkot to form an Israeli government; four nations urge
Israel to open Gaza aid; France hit by a fourth weekend of protests;
COP31 climate talks run into overtime; US details $12bn in Venezuelan oil
revenue; Al-Shabaab claims a mass ambush on Somali troops.

## Run

```sh
python3 draw.py        # renders entry.png (1024x1024) in this directory
MAKEFUN_OUTPUT_DIR=/path/to/out python3 main.py   # copies entry.png there
```

`draw.py` uses only Pillow and the DejaVu fonts shipped with the system
(`/usr/share/fonts/truetype/dejavu/`); `main.py` uses only the standard
library. Rendering is deterministic: running `draw.py` twice produces a
byte-identical `entry.png`.

## Files

- `draw.py` — draws the front page and writes `entry.png`.
- `main.py` — copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`.
- `entry.png` — the rendered front page (1024×1024 PNG).
- `LICENSE` — MIT.
