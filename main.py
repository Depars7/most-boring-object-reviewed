"""Most Boring Object, Reviewed in One Line — entry writer.

Writes one funny, true one-line review of the dustpan to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

# The review, assembled from three parts so the turn lands early and the
# last words sharpen it (judge criteria 4 and 5).
PARTS = [
    "The dustpan's entire career is cleaning up after the broom,",
    "and it still can't get the last line of dust.",
]


def entry_line() -> str:
    """Return the final one-line review (verified: 105 chars, one line)."""
    return " ".join(PARTS)


def main() -> None:
    line = entry_line()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line.strip() == line and "\n" not in line, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
