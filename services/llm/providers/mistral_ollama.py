import httpx

from core.config import get_settings
from services.llm.provider import LLMProvider


class MistralOllamaProvider(LLMProvider):
    def __init__(self):
        settings = get_settings()

        self.model = settings.ollama_model
        self.base_url = settings.ollama_base_url

    async def complete(self, *, system: str, user: str) -> str:
        prompt = f"""SYSTEM:
{system}

USER:
{user}
"""

        timeout = httpx.Timeout(300.0)

        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
            )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "")