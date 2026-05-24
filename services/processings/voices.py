from services.llm.client import LLMClient


class VoiceEngine:
    def __init__(self) -> None:
        self.llm = LLMClient()

    async def ops(self, content: str) -> str:
        return await self.llm.complete(
            system="You are OPS voice. Be technical and precise.",
            user=content,
        )

    async def audit(self, content: str) -> str:
        return await self.llm.complete(
            system="You are AUDIT voice. Be critical and structured.",
            user=content,
        )

    async def arlette(self, content: str) -> str:
        return await self.llm.complete(
            system="You are ARLETTE. You are satirical and narrative.",
            user=content,
        )