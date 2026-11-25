"""Write the Dad Joke Showdown entry using only the Python standard library."""

import os
from pathlib import Path


JOKE = "I put a graduation cap on the gravy boat. It majored in pouring decisions."

if "\n" in JOKE or "\r" in JOKE or len(JOKE) > 200:
    raise ValueError("JOKE must be a single line of at most 200 characters")


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
