import httpx
import structlog

from services.llm.provider import LLMProvider
from core.config import get_settings

logger = structlog.get_logger()


class MistralOllamaProvider(LLMProvider):
    def __init__(self) -> None:
        self.settings = get_settings()
        self.client = httpx.AsyncClient()

    async def complete(self, system: str, user: str) -> str:
        url = f"{self.settings.ollama_base_url}/api/generate"

        payload = {
            "model": "mistral",
            "prompt": f"{system}\n\n{user}",
            "stream": False,
        }

        # 👇 IMPORTANT : on neutralise UNIQUEMENT le read timeout
        timeout = httpx.Timeout(
            connect=10.0,   # garde un minimum de sécurité réseau
            read=None,      # 🔥 autorise inference infinie
            write=30.0,     # protection basique payload
            pool=30.0,      # évite blocage pool connection
        )

        logger.info(
            "calling_ollama",
            url=url,
            timeout="read=None"
        )

        try:
            response = await self.client.post(
                url,
                json=payload,
                timeout=timeout,
            )
            response.raise_for_status()

        except httpx.HTTPError as e:
            logger.exception("ollama_request_failed", error=str(e))
            raise

        data = response.json()

        return data["response"]