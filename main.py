"""Entry for make.fun bounty u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.

Writes the chosen excuse, byte-identical with no trailing newline, to
entry.txt inside the directory named by MAKEFUN_OUTPUT_DIR.
Python standard library only.
"""

import os

ENTRY = (
    "I delegated the deadline to a subagent. "
    "It delegated it back. "
    "We have been very productive at delegating it ever since."
)


def main():
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
