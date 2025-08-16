"""A minimal in‑memory vector store used for semantic similarity search.

This module intentionally keeps the implementation tiny and dependency free
(except for NumPy) while mimicking the interface of a typical vector database.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

import numpy as np


@dataclass
class SimpleVectorDB:
    """Very small in‑memory vector database.

    Texts are embedded using a crude hashing scheme based on character codes.
    While not suitable for production, it suffices for demonstration and unit
    testing of the high level pipeline.
    """

    texts: List[str] = field(default_factory=list)
    vectors: List[np.ndarray] = field(default_factory=list)

    def _embed(self, text: str) -> np.ndarray:
        codes = [ord(c) for c in text.lower()]
        # Use a fixed length embedding: first 32 characters, padded with zeros.
        vec = np.zeros(32, dtype=float)
        trunc = codes[:32]
        vec[: len(trunc)] = trunc
        return vec

    def add(self, text: str) -> None:
        self.texts.append(text)
        self.vectors.append(self._embed(text))

    def similarity_search(self, query: str, top_k: int = 1) -> List[Tuple[str, float]]:
        if not self.texts:
            return []
        qvec = self._embed(query)
        sims = [float(np.dot(qvec, vec)) for vec in self.vectors]
        idxs = np.argsort(sims)[::-1][:top_k]
        return [(self.texts[i], sims[i]) for i in idxs]


__all__ = ["SimpleVectorDB"]
