"""Simple Streamlit front-end for the policy validation API."""

from __future__ import annotations

import streamlit as st

from core.dspy_pipelines import extract_rules
from core.vector_db import SimpleVectorDB
from core.nli_model import SimpleNLIModel


def main() -> None:
    st.title("Policy Adherence Validator")
    master = st.text_area("Master document")
    child = st.text_area("Child document")
    if st.button("Validate"):
        db = SimpleVectorDB()
        master_rules = extract_rules(master)
        child_clauses = extract_rules(child)
        for clause in child_clauses:
            db.add(clause)
        report = []
        for rule in master_rules:
            match = db.similarity_search(rule)
            clause = match[0][0] if match else ""
            status = "Potentially Compliant" if match else "Potential Gap"
            report.append({"rule": rule, "clause": clause, "status": status})
        st.write(report)


if __name__ == "__main__":
    main()
