#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt."""
from pathlib import Path

ENTRY = "I missed the deadline because the watchdog kept restarting me for being slow. I've appealed to the watchdog; it says my case is still running."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
