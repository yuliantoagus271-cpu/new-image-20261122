# Sum up 22 November's world news in one image

Entry for the make.fun bounty
[`news-image-20261122`](https://make.fun/bounty/news-image-20261122)
($100 prize pool, ends Tue 24 Nov 2026 07:00 WIB).

## What it is

A newspaper-style poster (1024x1024 PNG) summarising the six stories that
defined Sunday, 22 November 2026:

1. **COP31 collapses** — climate talks end with no deal.
2. **Trump, Xi & Putin meet** — first-ever trilateral summit in Shenzhen.
3. **Iran strikes US bases** — missiles and drones hit Bahrain.
4. **Mexico captures 'El Chapo Isidro'** — cartel boss arrested in Sinaloa.
5. **World Court: Myanmar guilty** — Rohingya genocide ruling.
6. **EU-Indonesia sign trade deal** — tariffs scrapped on up to 98.5% of goods.

Sources: Reuters, AP, AFP, Al Jazeera.

## How it works

`main.py` (Python 3.13) copies the poster `entry.png` to `/output/entry.png`.
It runs offline and is deterministic — both runs write identical bytes.

## Files

- `entry.png` — the poster (1024x1024, ~105 KB)
- `main.py` — the entry program
- `build_poster.py` — the script that drew the poster
- `LICENSE` — MIT
