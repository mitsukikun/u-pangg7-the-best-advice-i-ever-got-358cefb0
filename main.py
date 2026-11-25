#!/usr/bin/env python3
"""Entry for make.fun competition 'The Best Advice I Ever Got'.

Writes exactly one sentence (103 characters) to /output/entry.txt.
Standard library only, no network.
"""

import os

SENTENCE = "My grandmother said, 'Do the small work well, and the big work will trust you,' and I still live by it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
