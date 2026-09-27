"""Student-facing application logic for Lab 02."""

from __future__ import annotations

from src.config import load_config
from src.mock_provider import MockProvider
from src.openai_provider import OpenAIProvider


def validate_prompt(prompt: str) -> str:
    """Validate and normalize a user prompt."""
    # TODO: implement this function.
    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string.")

    normalized_prompt = prompt.strip()
    if not normalized_prompt:
        raise ValueError("Prompt must not be empty.")
    if len(normalized_prompt) > 4000:
        raise ValueError("Prompt must not exceed 4000 characters.")
    return normalized_prompt


def create_provider(config: dict):
    """Select and instantiate the configured provider."""
    # TODO: implement this function.
    provider_name = str(config.get("LLM_PROVIDER", "mock")).strip().lower()
    if provider_name == "mock":
        return MockProvider()
    if provider_name == "openai":
        api_key = config.get("OPENAI_API_KEY", "")
        model = config.get("OPENAI_MODEL", "")
        if not isinstance(api_key, str) or not api_key.strip():
            raise ValueError("OPENAI_API_KEY is required when LLM_PROVIDER is openai.")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("OPENAI_MODEL is required when LLM_PROVIDER is openai.")
        return OpenAIProvider(api_key=api_key, model=model)
    raise ValueError(f"Unsupported LLM_PROVIDER: {provider_name!r}.")


def generate_response(prompt: str) -> dict:
    """Generate a normalized response for a user prompt."""
    # TODO: implement this function.
    normalized_prompt = validate_prompt(prompt)
    config = load_config()
    provider = create_provider(config)
    response = provider.generate(normalized_prompt)
    return {
        "text": response.text,
        "provider": response.provider,
        "model": response.model,
    }


def main() -> None:
    """Simplified CLI entry point for the lab."""
    print("LLMOps Lab 02")

    try:
        config = load_config()
    except NotImplementedError:
        print("Complete the TODO implementations in src/config.py, src/provider.py, src/mock_provider.py, src/openai_provider.py, and src/app.py before running this demo.")
        return

    print("Provider:", config.get("LLM_PROVIDER", "mock"))

    prompt = input("\nEnter prompt:\n> ")

    try:
        response = generate_response(prompt)
    except NotImplementedError:
        print("Complete the TODO implementations in src/config.py, src/provider.py, src/mock_provider.py, src/openai_provider.py, and src/app.py before running this demo.")
        return

    print("\nResponse:")
    print(response["text"])


if __name__ == "__main__":
    main()
