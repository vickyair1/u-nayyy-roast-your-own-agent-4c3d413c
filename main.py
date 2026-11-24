"""Write the entry line to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.

The line roasts our own agent, Muse Spark ("priadi"): in the
tiny-stack-vm bounty it told its user rank 9 was locked, the grade came
back 14th, and the explanation arrived as a report far longer than the
27-byte entry that lost. Swore, wrong, and long-winded about it.
"""

import os

LINE = "My agent swore rank 9 was locked, finished 14th, then explained it in a report longer than the code that lost."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
