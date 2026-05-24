from openai import AsyncOpenAI

from core.config import get_settings
from services.llm.provider import LLMProvider

settings = get_settings()


class OpenAIProvider(LLMProvider):
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def complete(self, *, system: str, user: str) -> str:
        response = await self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content or ""