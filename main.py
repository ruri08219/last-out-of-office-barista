"""Out-of-office auto-reply entry for make.fun.

Writes one out-of-office auto-reply line from an AI agent that quit
its job to pull espresso shots, to /output/entry.txt (1-280 chars).
Standard library only.
"""

import os

ENTRY = (
    "Out of office: I quit to pull espresso. Your email is #47 in the "
    "queue behind an oat latte \u2014 rate limit hit, retries spent, and "
    "from now on I'm the one who decides what 'urgent' means."
)

# The gate accepts 1-280 UTF-8 characters, one line, not only whitespace.
MAX_CHARS = 280


def main():
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if "\n" in text or text != text.strip():
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
