"""One-Line Laugh-Off — makefun-laugh-off-01."""

ENTRY = "My smart fridge heard me sleep-talk 'I'm in a pickle' at 3 a.m. and ordered $87 of pickles — I now own 214 jars, and the delivery driver took out a restraining order on me."


def main():
    print(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
