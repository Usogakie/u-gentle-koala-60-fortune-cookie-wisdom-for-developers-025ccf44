"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
entry.txt in the output directory. Deterministic: no network, no clock,
no randomness, no input. The same line is written on every run.
"""

import os

FORTUNE = (
    "Your future self is already debugging the shortcut "
    "you are about to take."
)


def main() -> None:
    # The gate refuses anything outside 1-120 characters or only
    # whitespace, so fail loudly here instead of shipping a bad file.
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, "fortune must be 1-120 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
