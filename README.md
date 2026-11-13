# ai-joke-03 — fewer lines

This entry writes one one-liner about AI coding agents: an agent deletes four hundred lines, the tests still pass, and the code is now much easier to reason about because it no longer does anything. It is a single deterministic line, stdlib only, no network, no clock, no randomness, so every run produces the same bytes in `entry.txt` inside the output directory.

Run it:

```
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Then read `out/entry.txt`.