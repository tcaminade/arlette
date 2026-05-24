import structlog

from core.config import get_settings
from services.llm.provider import LLMProvider
from services.llm.providers.mistral_ollama import MistralOllamaProvider
from services.llm.providers.mock_provider import MockProvider
from services.llm.providers.openai_provider import OpenAIProvider

logger = structlog.get_logger()


def create_llm_provider() -> LLMProvider:
    settings = get_settings()

    provider: str = settings.llm_provider

    logger.info("llm_provider_selected", provider=provider)

    if provider == "mistral":
        return MistralOllamaProvider()

    if provider == "openai":
        return OpenAIProvider()

    return MockProvider()