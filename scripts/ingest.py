"""Script for ingesting policy documents into the vector DB."""

from __future__ import annotations

from pathlib import Path

from core.dspy_pipelines import extract_rules
from core.vector_db import SimpleVectorDB


def ingest_file(path: Path, db: SimpleVectorDB) -> None:
    text = path.read_text()
    for rule in extract_rules(text):
        db.add(rule)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Ingest documents into vector DB")
    parser.add_argument("file", type=Path)
    args = parser.parse_args()

    db = SimpleVectorDB()
    ingest_file(args.file, db)
    print(f"Ingested {len(db.texts)} rules")
