# Automated Policy Adherence Validation

This repository contains a minimal implementation of an automated policy
adherence validation system.  It follows the phased design laid out in the
project brief and includes utilities for:

* extracting rules from policy documents using deontic markers
* building small knowledge graphs from the extracted rules
* storing and searching rule embeddings in a tiny in‑memory vector database
* serving a FastAPI API and a Streamlit based front‑end

The code is purposely lightweight so that the core ideas can be explored without
requiring heavy external dependencies.

## Structure

```
app/            – FastAPI application and Streamlit front‑end
config/         – project configuration
core/           – core logic such as rule extraction and graph building
scripts/        – helper scripts for ingestion and data generation
tests/          – unit tests for the core components
```

## Development

Install dependencies and run tests:

```bash
pip install -r requirements.txt
pytest
```

Run the API locally:

```bash
python -m app.main
```

Run the Streamlit front‑end:

```bash
streamlit run app/frontend.py
```
