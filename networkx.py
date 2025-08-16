"""Tiny subset of the networkx API used for unit testing."""

from __future__ import annotations

from collections import defaultdict


class DiGraph:
    def __init__(self) -> None:
        self._edges = defaultdict(dict)

    def add_edge(self, u, v, **attrs):
        self._edges[u][v] = attrs

    def has_edge(self, u, v) -> bool:
        return v in self._edges.get(u, {})

    def __getitem__(self, item):
        return self._edges[item]

