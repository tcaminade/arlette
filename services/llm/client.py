from services.llm.factory import create_llm_provider


class LLMClient:
    def __init__(self):
        self.provider = create_llm_provider()

    async def complete(self, *, system: str, user: str) -> str:
        return await self.provider.complete(system=system, user=user)