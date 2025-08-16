"""Entry point for running the FastAPI application."""

from __future__ import annotations

from .api import app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
