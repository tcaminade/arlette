from services.llm.factory import create_llm_provider
from services.llm.provider import LLMProvider


class LLMClient:
    def __init__(self) -> None:
        self.provider: LLMProvider = create_llm_provider()

    async def complete(self, system: str, user: str) -> str:
        return await self.provider.complete(system=system, user=user)