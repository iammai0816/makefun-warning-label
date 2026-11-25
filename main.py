#!/usr/bin/env python3
"""Write one original warning label for humans to /output/entry.txt.

The program is deterministic: it always emits the same single line,
the entry itself, into entry.txt under MAKEFUN_OUTPUT_DIR.

The line is judged as a printed safety warning label for every human:
funny first, plausible second, with the laugh landing in the last few
words. It must stay a single line of 1-160 characters, so the guards
below reject anything outside that range or with stray whitespace.
"""

import os

LABEL = (
    "WARNING: May reply to a text three days later with "
    "'haha sorry just saw this.' It saw it instantly."
)


def main() -> None:
    # Guard: the entry must be a single line of 1-160 chars before writing.
    assert "\n" not in LABEL, "entry must be a single line"
    assert LABEL == LABEL.strip(), "entry must not carry stray whitespace"
    assert 1 <= len(LABEL) <= 160, f"entry length out of range: {len(LABEL)} chars"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(LABEL)


if __name__ == "__main__":
    main()
