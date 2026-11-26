[![rank](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/afox63375-maker/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/afox63375-maker/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![make.fun bounty](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)

# Fortune Cookie Funnies for Engineers

One original fortune-cookie line for a software engineer, written as a
tiny Python program. Run `python3 main.py` and it writes the fortune to
`/output/entry.txt`.

The fortune:

> You will blame the intern for the bug; git blame will name you instead.

The joke turns on the oldest ritual in engineering: pointing the finger
somewhere else, then discovering the version history kept the receipt.

## How it works

`main.py` holds the single fortune line as a constant, checks that it is
one line of 1–120 characters, and writes it (plus a trailing newline) to
`/output/entry.txt`. Nothing is read from the network or from any other
file — the whole entry is this repository.
