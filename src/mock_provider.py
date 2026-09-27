"""Mock provider for Lab 02."""

from __future__ import annotations

from src.models import LLMResponse
from src.provider import BaseProvider


class MockProvider(BaseProvider):
    """Deterministic provider used for testing and local development."""

    def generate(self, prompt: str) -> LLMResponse:
        """Return a deterministic mock response."""
        # TODO: implement this method.
        normalized_prompt = prompt.strip()
        return LLMResponse(
            text=f"Mock response to: {normalized_prompt}",
            provider="mock",
            model="mock-model",
            usage=None,
        )
