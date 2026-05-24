from typing import Protocol


class LLMProvider(Protocol):
    async def complete(self, system: str, user: str) -> str:
        """
        Returns the model output as plain text.
        """
        ...