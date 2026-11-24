# SPDX-License-Identifier: MIT
"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for a ridiculous invention that fixes a tiny
everyday annoyance, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The pitch is one sentence, at most 220 characters.
"""

import os

# The invention: the Bedtime Bouncer. The annoyance is the nightly
# "just one more video" loop that keeps you up far past bedtime. The fix
# is a lamp that dims a little more with every excuse, then physically
# escorts your phone to its charger, like a bouncer clearing the club.
# One sentence, one lamp, one tiny intervention.
PITCH = (
    "Behold the Bedtime Bouncer, a lamp that dims a little more every time "
    "you whisper 'just one more video', then escorts your phone to the "
    "charger like a tiny bouncer clearing the club at closing time."
)


def build_pitch() -> str:
    """Assemble the one-sentence pitch from its parts."""
    return PITCH.strip()


def validate_pitch(pitch: str) -> None:
    """The gate: one sentence, 1 to 220 characters, not only whitespace."""
    stripped = pitch.strip()
    if not stripped:
        raise ValueError("pitch must not be blank")
    if not (1 <= len(stripped) <= 220):
        raise ValueError(f"pitch is {len(stripped)} chars, must be 1-220")
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("pitch must be exactly one sentence")


def write_entry(pitch: str, out_dir: str) -> str:
    """Write the pitch to entry.txt inside out_dir; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(pitch + "\n")
    return path


def main() -> None:
    pitch = build_pitch()
    validate_pitch(pitch)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(pitch, out_dir)


if __name__ == "__main__":
    main()
