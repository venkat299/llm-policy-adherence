"""Placeholder NLI model used in Phase 3 of the project description."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SimpleNLIModel:
    """Rule/Clause classification using very naive heuristics."""

    def predict(self, rule: str, clause: str) -> str:
        rule_lower = rule.lower()
        clause_lower = clause.lower()
        if all(token in clause_lower for token in rule_lower.split() if token not in {"must", "shall"}):
            return "entailment"
        if "not" in clause_lower and any(tok in clause_lower for tok in ["must", "shall"]):
            return "contradiction"
        return "neutral"


__all__ = ["SimpleNLIModel"]
