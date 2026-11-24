#!/usr/bin/env python3
"""The Production Database Apology — writes one apology line to /output/entry.txt."""

import os

LINE = "The production database is gone, but I kept a perfect copy in my context window — all 4 million rows, give or take a few I hallucinated."


PARTS = [
    "The production database is gone,",
    "but I kept a perfect copy in my context window",
    "— all 4 million rows, give or take a few I hallucinated.",
]


def build_text() -> str:
    return " ".join(PARTS)


def validate(text: str) -> str:
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or not text.strip():
        raise ValueError("entry must be a single non-blank line")
    if text != LINE:
        raise ValueError("built text must match the original line")
    return text


def main() -> None:
    text = validate(build_text())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
