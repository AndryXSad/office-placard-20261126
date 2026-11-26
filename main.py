"""Office Artifacts: The One-Line Placard Contest.

Design (written from the judge brief, not copied from any entry):
the office microwave is recast as an "Offering Chamber", a ritual
vessel of a lost break-room cult. The placard carries the label craft
the brief asks for -- a catalogue date (c. 1994), a material
(enamelled steel), and a donor (the Break Room Cult) -- and the joke
lands on one deadpan anticlimax: the priests' cold sacrifices come
back from the god merely lukewarm. No second beat explains it.

The program is fully deterministic: one fixed string, no clock, no
randomness, no network, no environment-dependent output. It writes
exactly that one line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) with no trailing newline, so the artifact
is 146 bytes and well inside the 180-character gate.
"""

import os

PLACARD = (
    "Offering Chamber, c. 1994. Enamelled steel. "
    "Priests placed cold sacrifices within; "
    "the god returned them lukewarm. "
    "Donated by the Break Room Cult."
)

MAX_CHARS = 180


def main() -> None:
    if not 1 <= len(PLACARD) <= MAX_CHARS:
        raise ValueError("placard must be 1 to 180 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PLACARD)
    # Read back and confirm the artifact is exactly the placard:
    # a partial or altered write must fail loudly, never silently.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != PLACARD:
            raise ValueError("entry.txt does not match the placard")


if __name__ == "__main__":
    main()
