"""Utilities for rule extraction using simple deontic marker matching.

This module provides a light‑weight stand in for the DSPy based pipelines
outlined in the project specification.  The goal is to provide an easily
unit‑testable baseline implementation without requiring the DSPy package or
external model calls.
"""

from __future__ import annotations

import re
from typing import List

# Regex that matches common deontic markers signalling obligations or
# prohibitions.
DEONTIC_MARKERS = re.compile(
    r"\b(must|shall|may not|shall not|must not|prohibited|required)\b",
    re.IGNORECASE,
)


def extract_rules(policy_text: str) -> List[str]:
    """Extract sentences containing deontic markers.

    Parameters
    ----------
    policy_text: str
        Raw text of a policy document.

    Returns
    -------
    List[str]
        Sentences that contain one of the recognised deontic markers.
    """
    # Split on sentence boundaries.  This heuristic is intentionally simple but
    # works well for the short test snippets used in the unit tests.
    sentences = re.split(r"(?<=[.!?])\s+", policy_text.strip())
    rules = [s.strip() for s in sentences if DEONTIC_MARKERS.search(s)]
    return rules


__all__ = ["extract_rules"]
