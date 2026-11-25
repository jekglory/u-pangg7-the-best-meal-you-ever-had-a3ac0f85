"""The Best Meal You Ever Had entry.

Writes exactly one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). Pure Python 3.13 standard library, deterministic: the same fixed
sentence on every run, no randomness, no clock, no network, no input. The
judge reads the sentence cold, so it carries its own dish, place, sensory
detail and memory in one sentence.
"""

import os

SENTENCE = "My grandmother's rendang, slow-cooked six hours in her Jakarta kitchen, fell apart on my tongue and tasted like every Sunday of my childhood at once."
# 149 characters: one sentence, one dish, one kitchen, one memory — under
# the 200-character ceiling with room to spare.


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Only the contents are cleared by the caller when needed; never delete
    # the output directory itself — the grader owns it.
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the gate counts the file's characters (1-200),
    # so the file holds exactly the sentence, nothing extra.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
