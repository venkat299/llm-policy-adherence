"""Simple knowledge graph construction utilities.

The real project envisions rich subject‑action‑object extraction and graph
storage.  For the purposes of this repository we provide a minimal yet usable
implementation relying only on ``networkx``.
"""

from __future__ import annotations

import re
from typing import Iterable, Tuple

import networkx as nx

# Re‑use the deontic markers from the extraction module for consistency.
_DEONTIC_WORDS = [
    "must",
    "shall",
    "may not",
    "shall not",
    "must not",
    "prohibited",
    "required",
]


def _parse_rule(rule: str) -> Tuple[str, str, str] | None:
    """Very small heuristic subject/action/object parser.

    The parser looks for the first occurrence of a deontic marker.  Text before
    the marker is treated as the *subject*, the marker itself becomes the
    *action*, and the remainder of the sentence is the *object*.
    """
    lower = rule.lower()
    for word in _DEONTIC_WORDS:
        if word in lower:
            parts = lower.split(word, 1)
            subject = parts[0].strip().rstrip(", ")
            obj = parts[1].strip()
            return subject, word, obj
    return None


def build_graph(rules: Iterable[str]) -> nx.DiGraph:
    """Build a directed graph from iterable of rules.

    Each rule becomes an edge from subject -> object annotated with the action
    (deontic marker).  Nodes are created automatically as needed.
    """
    graph = nx.DiGraph()
    for rule in rules:
        parsed = _parse_rule(rule)
        if not parsed:
            continue
        subject, action, obj = parsed
        graph.add_edge(subject, obj, action=action)
    return graph


__all__ = ["build_graph"]
