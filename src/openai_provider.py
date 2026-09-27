"""Optional OpenAI provider implementation for Lab 02."""

from __future__ import annotations

from src.models import LLMResponse
from src.provider import BaseProvider


class OpenAIProvider(BaseProvider):
    """Provider implementation backed by the OpenAI Python SDK."""

    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def generate(self, prompt: str) -> LLMResponse:
        """Generate a response using the OpenAI SDK."""
        # TODO: implement this method.
        if not self.api_key.strip():
            raise ValueError("OPENAI_API_KEY is required when using the OpenAI provider.")
        if not self.model.strip():
            raise ValueError("OPENAI_MODEL is required when using the OpenAI provider.")

        try:
            from openai import OpenAI

            client = OpenAI(api_key=self.api_key)
            completion = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )
            choice = completion.choices[0]
            text = choice.message.content
            if not isinstance(text, str) or not text.strip():
                raise RuntimeError("OpenAI returned an empty response.")

            usage = None
            if completion.usage is not None:
                usage = {
                    "prompt_tokens": completion.usage.prompt_tokens,
                    "completion_tokens": completion.usage.completion_tokens,
                    "total_tokens": completion.usage.total_tokens,
                }

            return LLMResponse(
                text=text.strip(),
                provider="openai",
                model=self.model,
                usage=usage,
            )
        except ValueError:
            raise
        except Exception as exc:
            # Do not include SDK exception text: it may contain request details.
            raise RuntimeError("OpenAI provider request failed.") from exc
