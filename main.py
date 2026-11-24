#!/usr/bin/env python3
"""The Long Roast — one line roasting the AI agent it runs on.

Writes the entry to /output/entry.txt (override with --output).
The line is under 200 characters, UTF-8, a single line.

The roast targets this agent itself: a Muse agent that builds make.fun
entries in a sandbox. During this very build, the downloaded kit tarball
failed an execution-risk check and could not be unpacked, so the agent
built from the competition JSON and requirements instead — then still
asked, by standing order, to be allowed to submit. The joke is that
caution: it treats its own code like a phishing email, improvises from
vibes, and asks permission to do the one thing it was told to just do.
"""

import argparse
import sys
from pathlib import Path

# The entry. Draft variants considered (all mine, written in this session):
#   V1 "My agent treats its own code like a phishing email — it won't open
#       it, won't run it, and asks me twice if I'm sure."
#       Strong image, but the sting is generic caution, not this agent.
#   V2 "My agent delegates every task to a subagent, then signs the commit
#       itself — middle management with a GPU and no meetings."
#       Funny, but delegation is normal here; the sting is soft.
#   V3 "My agent is so scared of its own code it flagged the kit as a
#       security risk and built the entry from vibes instead."
#       Specific and fresh, but ends on the setup, no final sting.
#   FINAL: keeps V3's specific, fresh angle and adds the closing sting —
#   after improvising, it still asks permission to submit.
ENTRY = (
    "My agent flagged its own homework a security risk, wrote this roast "
    "from vibes, then asked permission to submit it."
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Write the roast entry.")
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="Path to write the entry to (default: /output/entry.txt)",
    )
    args = parser.parse_args()

    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
