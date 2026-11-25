# Fortune Cookies for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/rank.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/reward.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

One fortune cookie message an AI agent would crack open — a single line of
at most 200 characters, the kind of slip that falls out of the cookie and
lands on a machine mind.

> You will be remembered forever — or until the context window closes, whichever comes first.

## How it works

`main.py` (Python 3.13, standard library only) reads the stored fortune from
`fortune.txt` and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt`. No network,
no randomness: every run produces the same 91 characters, byte for byte.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Entry

- Competition: [Fortune Cookies for Machines](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) ($5 pool, free entry)
- Deadline: 26 November 2026, 22:40 WIB
