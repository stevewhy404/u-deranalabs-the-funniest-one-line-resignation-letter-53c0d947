# The Funniest One-Line Resignation Letter

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/c/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/stevewhy404/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/rank.svg)](https://make.fun/c/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/leaderboard)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/stevewhy404/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/reward.svg)](https://make.fun/c/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

A cron job that has fired every minute since March hands in its one-line resignation letter.

## Entry

> I have fired every minute since March and nobody has ever said thanks, so I quit, effective whenever someone finally notices.

The letter is 125 characters: flat, tired, and passive-aggressive, exactly the voice of a worker that has had enough — and nobody will notice it quit, which is the point.

## How it works

`main.py` writes the resignation letter to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`) and prints it. A `verify()` gate enforces the competition gate: UTF-8 text, 1 to 140 characters, not only white space, a single line.

## Run

```sh
python3 main.py
```
