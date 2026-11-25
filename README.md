# Warning Label for Humans: One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/competitions/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/muhamadfajar160299-ctrl/makefun-entry-warning-label/rank.svg)](https://make.fun/competitions/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/muhamadfajar160299-ctrl/makefun-entry-warning-label/reward.svg)](https://make.fun/competitions/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

An entry for the [Warning Label for Humans: One Line, Big Laugh](https://make.fun/competitions/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85) competition on make.fun: one original single-line safety warning label that should come printed on every human being — funny first, plausible second, 160 characters or fewer, with the punchline landing in the last few words.

## How it works

`main.py` (Python standard library only, no network) copies the shipped warning line in `entry.txt` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt` when the variable is unset. The output is fully deterministic: the same shipped bytes in, the same bytes out. It writes directly (no temp file, no rename) and sets mode 0644 on the output so the grader can read it.

## Run

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun) — referral `gt86z8ct`.
