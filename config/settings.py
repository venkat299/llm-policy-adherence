"""Central project configuration."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Settings:
    vector_db_path: str = "data/vector_db"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"


settings = Settings()
