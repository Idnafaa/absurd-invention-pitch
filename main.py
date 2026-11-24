# SPDX-License-Identifier: MIT
"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for a ridiculous invention that fixes a tiny
everyday annoyance, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The pitch is one sentence, at most 220 characters.
"""

import os

PITCH = (
    "Behold the Bedtime Bouncer, a lamp that dims a little more every time "
    "you whisper 'just one more video', then escorts your phone to the "
    "charger like a tiny bouncer clearing the club at closing time."
)


def main() -> None:
    pitch = PITCH.strip()
    assert pitch.count(".") == 1 and pitch.endswith("."), "must be one sentence"
    assert 1 <= len(pitch) <= 220, f"pitch is {len(pitch)} chars, must be <= 220"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(pitch + "\n")


if __name__ == "__main__":
    main()
