# Tuesday, 17 November 2026 — World News in One Image

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/reza0109/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/reza0109/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Entry for the make.fun bounty **"Sum up 17 November's world news in one image"**
(`news-image-20261117`).

## What it is

A 1024×1024 infographic summarising the world news of Tuesday, 17 November 2026
in five stories: the US strikes on Iranian missile sites after the Strait of
Hormuz tanker attacks, Ukraine's strike on the Crimean Bridge, the US losing
measles elimination status, the Western call for Israel to open Gaza crossings,
and Trump's trip to China for a trilateral summit. Every fact in the image was
cross-checked against Reuters, AP, ABC News, PAHO and the UN — no speculation,
no rumours, no casualty figures beyond what was reported.

## How the image was made

`entry.png` was rendered with [Pillow](https://python-pillow.org/) by the
reproducible script `draw.py` (fixed layout, Noto Sans fonts, no randomness,
no clock), then checked by eye for legibility: every headline fits on one line
and every summary fits its card with no overflow or clipping.

## How to run

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Running it
twice writes byte-identical output. To re-render the image from scratch:

```sh
python3 draw.py
```
