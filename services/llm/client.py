from core.config import get_settings

settings = get_settings()


class LLMClient:
    async def summarize(self, text: str) -> str:
        return f"[SUMMARY] {text[:120]}"

    async def arlette_voice(self, text: str) -> str:
        return f"[ARLETTE] {text[:200]}"