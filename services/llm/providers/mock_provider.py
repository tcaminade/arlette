from services.llm.provider import LLMProvider


class MockProvider(LLMProvider):
    async def complete(self, *, system: str, user: str) -> str:
        return f"[MOCK RESPONSE]\nSYSTEM:{system[:50]}\nUSER:{user[:50]}"