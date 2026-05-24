import structlog

from core.config import get_settings

from services.llm.providers.mistral_ollama import MistralOllamaProvider
from services.llm.providers.openai_provider import OpenAIProvider
from services.llm.providers.mock_provider import MockProvider
from services.llm.provider import LLMProvider

logger = structlog.get_logger()

def create_llm_provider():
    settings = get_settings()

    provider = getattr(settings, "llm_provider", "mistral")

    logger.info("llm_provider_selected", provider=provider)

    if provider == "mistral":
        return MistralOllamaProvider()

    if provider == "openai":
        return OpenAIProvider()

    if provider == "mock":
        return MockProvider()

    raise ValueError(f"Unknown LLM provider: {provider}")