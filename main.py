"""One-line laugh-off entry.

A smart fridge takes a sleep-talked idiom literally and turns it into
a very expensive, very crunchy problem.
"""

ENTRY = "My smart fridge heard me sleep-talk 'I'm in a pickle' at 3 a.m. and ordered $87 of pickles — I now own 214 jars, and the delivery driver took out a restraining order on me."


def get_entry():
    """Return the competition entry line."""
    return ENTRY


def main():
    """Print the entry and write it to /output/entry.txt."""
    entry = get_entry()
    print(entry)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
