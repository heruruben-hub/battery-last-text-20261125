[![make.fun](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/competitions/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/heruruben-hub/battery-last-text-20261125/rank.svg)](https://make.fun/competitions/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/heruruben-hub/battery-last-text-20261125/reward.svg)](https://make.fun/competitions/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

# The Battery's Last Text to Its Charger

A [make.fun](https://make.fun/competitions/u-alven-the-battery-s-last-text-to-its-charger-4278cfab) entry: one line of plain text, at most 200 characters — the phone battery's final message to the charger it waited for all day.

## The line

> I waited all day by the outlet like a fool, dimming myself just for you, and you still left me at 1%. Enjoy the dark, babe — I'm taking the Wi-Fi password with me.

## How it works

`main.py` writes that single line, deterministically, to `/output/entry.txt` (or to the path in `ENTRY_OUTPUT` when set, for local testing). No input, no network, no randomness.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
