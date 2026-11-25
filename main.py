"""Make the AI Judge Laugh — an office-life one-liner for make.fun.

Office printers have a sense of occasion: they only jam when the deadline
is today. This entry turns that universal experience into a single joke
and hands it to the judge as one line of text under 200 characters.
"""

import os
import sys

MAX_LEN = 200

ENTRY = (
    "Our office printer only jams on deadline day, which is why my review "
    "now lists 'printer whisperer' under core skills."
)


def get_entry():
    """The joke, with surrounding whitespace removed."""
    return ENTRY.strip()


def write_entry():
    joke = get_entry()
    if len(joke) < 1 or len(joke) > MAX_LEN:
        print("entry must be 1-200 characters", file=sys.stderr)
        sys.exit(1)
    if "\n" in joke:
        print("entry must be a single line", file=sys.stderr)
        sys.exit(1)
    directory = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    dest = os.path.join(directory, "entry.txt")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(joke)
    return dest


def main():
    dest = write_entry()
    print(f"wrote {dest} ({len(get_entry())} chars)")


if __name__ == "__main__":
    main()
