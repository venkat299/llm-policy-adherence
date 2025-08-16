"""FastAPI endpoints for policy validation."""

from __future__ import annotations

from typing import List, Optional

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

from core.dspy_pipelines import extract_rules
from core.vector_db import SimpleVectorDB

router = APIRouter()
vector_db = SimpleVectorDB()


class DocumentPair(BaseModel):
    master_text: str
    child_text: str


@router.post("/validate-documents")
def validate_documents(payload: DocumentPair) -> dict:
    master_rules = extract_rules(payload.master_text)
    child_clauses = extract_rules(payload.child_text)
    for clause in child_clauses:
        vector_db.add(clause)
    report: List[dict] = []
    for rule in master_rules:
        matches = vector_db.similarity_search(rule, top_k=1)
        if matches:
            clause, _score = matches[0]
            status = "Potentially Compliant"
        else:
            clause, status = None, "Potential Gap"
        report.append({"rule": rule, "clause": clause, "status": status})
    return {"report": report}


app = FastAPI(title="Policy Adherence API")
app.include_router(router)
