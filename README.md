# Dad Joke Showdown

[![make.fun bounty](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/adheyusuf230801-ship-it/u-mfnakmal-dad-joke-showdown-1d2ce3e5-codex/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard)
[![Reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/adheyusuf230801-ship-it/u-mfnakmal-dad-joke-showdown-1d2ce3e5-codex/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

> I put a graduation cap on the gravy boat. It majored in pouring decisions.

**74 characters**, including spaces and punctuation. The entry is one line, encoded as UTF-8 without a trailing newline.

## Drafts and selection

Six drafts written for this entry. Scores are editorial judgments from 1 (weak) to 5 (strong), compared in the competition's stated priority order: table-ready dad joke, clear pun, freshness, tightness with the punchline last, and natural delivery aloud. Freshness scores describe the drafts, not a claim of verified worldwide uniqueness.

| Draft | Characters | Table-ready | Clear pun | Freshness | Tightness | Aloud |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **I put a graduation cap on the gravy boat. It majored in pouring decisions.** | 74 | 5 | 5 | 4 | 5 | 5 |
| I gave the bread basket a bedtime. Those rolls need to rise early. | 66 | 5 | 5 | 3 | 5 | 5 |
| I put a tiny microphone beside the mashed potatoes. It was time to hear from the other side. | 92 | 5 | 4 | 4 | 4 | 5 |
| I served dinner on graph paper. My wife said I had finally plotted a decent meal. | 81 | 4 | 4 | 4 | 4 | 5 |
| I made a spreadsheet for the leftovers. My wife said I was overdoing it. I said, "Just keeping stock." | 102 | 4 | 4 | 3 | 3 | 5 |
| I put a tiny ladder in the gravy boat. The recipe said to bring it up to a simmer. | 82 | 5 | 3 | 4 | 4 | 5 |

The graduation-cap joke wins on freshness after tying the bread-basket joke on the first two criteria. Its dinner-table prop sets up the final pun: "pouring decisions" sounds like "poor decisions."

## Run

Target: **Python 3.13**, standard library only. No installation or network access required.

```sh
python3 main.py
```

The program creates `/output` if necessary and writes `/output/entry.txt`. It raises `ValueError` if `JOKE` contains a carriage return or newline, or exceeds 200 characters.

For local environments where `/output` is unavailable, select a writable directory:

```sh
OUTPUT_DIR=./output python3 main.py
```

This optional override changes only the output directory; the submitted text is identical.

## License

MIT; see [LICENSE](LICENSE).
