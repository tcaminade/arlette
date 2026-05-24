from services.llm.client import LLMClient
from prompts.load import load_prompt


class VoiceEngine:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    async def ops(self, text: str) -> str:
        return await self.llm.complete(
            system=load_prompt("prompts/voices/ops.txt"),
            user=text,
        )

    async def audit(self, text: str) -> str:
        return await self.llm.complete(
            system=load_prompt("prompts/voices/audit.txt"),
            user=text,
        )

    async def arlette(self, text: str) -> str:
        return await self.llm.complete(
            system=load_prompt("prompts/voices/arlette.txt"),
            user=text,
        )