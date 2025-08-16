"""Generate synthetic (rule, clause, label) triplets for NLI fine tuning."""

from __future__ import annotations

import csv
from typing import Iterable


EXAMPLE_RULES = [
    "Banks must maintain a CRAR of 9%.",
]


def generate_examples() -> Iterable[tuple[str, str, str]]:
    for rule in EXAMPLE_RULES:
        yield rule, "Our bank maintains a CRAR of 10%.", "entailment"
        yield rule, "We keep a CRAR of 8%.", "contradiction"
        yield rule, "We review assets quarterly.", "neutral"


if __name__ == "__main__":
    with open("synthetic_data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["rule", "clause", "label"])
        for row in generate_examples():
            writer.writerow(row)
    print("Wrote synthetic_data.csv")
