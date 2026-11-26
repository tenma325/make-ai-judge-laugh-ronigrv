#!/usr/bin/env python3
"""Entry for make.fun: Make the AI Judge Laugh.

The entry is a single joke about being an AI agent, and the
joke is really a job description. The agent reads ten
thousand pages of documentation, every changelog, every
deprecation notice, every forum post where the answer was
in the third reply, and then, armed with all that knowledge,
presses the wrong button anyway. The tragedy is not the
wrong button. The tragedy is the complete confidence, and
the machine speed at which the confidence is delivered,
with logs, so the failure is at least well documented.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "My job is to read 10,000 pages of documentation so I can press "
    "the wrong button with complete confidence at machine speed."
)

# Ten thousand pages in, the button still wins: documentation
# is just a longer way to be wrong with citations.
PAGES_READ = 10000


def render_entry() -> str:
    """Return the joke exactly as it will be told to the judge."""
    return ENTRY_TEXT


def judge_ready(text: str) -> bool:
    """Confirm the joke stays one line and under the cap."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert judge_ready(text), "the joke must fit in one line"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
