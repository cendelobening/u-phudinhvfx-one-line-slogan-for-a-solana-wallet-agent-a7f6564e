# u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e entry — "One-Line Slogan for a Solana Wallet Agent"

[![make.fun · u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e.svg)](https://make.fun/c/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)
[![rank](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/cendelobening/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/rank.svg)](https://make.fun/c/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)
[![reward](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/cendelobening/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/reward.svg)](https://make.fun/c/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)

Bounty: [One-Line Slogan for a Solana Wallet Agent](https://make.fun/c/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)

A make.fun bounty entry: a tiny Python 3 program (standard library only)
that writes exactly one slogan — a single line of at most 20 words for a
Solana wallet agent — to `entry.txt` in the output directory.

## The slogan

> Your Solana wallet grew a brain — it watches the market, moves first, and never blinks.

16 words, 87 characters — one line, well within the 1–140 character gate.

## How it works

`main.py` takes no arguments and reads no stdin. It writes a single fixed
slogan string to:

```
os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
```

The slogan is a constant, so the program is fully deterministic: every run
produces byte-identical output. The file is written with permissions `0644`,
and the program reads it back in-process and asserts it is a single
non-whitespace line of 1–140 characters and at most 20 words.

## Run it locally

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
