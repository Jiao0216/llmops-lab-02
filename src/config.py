"""Student-facing configuration helpers for Lab 02."""

from __future__ import annotations

import os


def load_config() -> dict:
    """
    Load configuration from environment variables.

    Expected keys:
    - LLM_PROVIDER
    - OPENAI_API_KEY
    - OPENAI_MODEL
    """
    # TODO: implement this function.
    return {
        "LLM_PROVIDER": os.getenv("LLM_PROVIDER", "mock").strip().lower() or "mock",
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
        "OPENAI_MODEL": os.getenv("OPENAI_MODEL", ""),
    }
