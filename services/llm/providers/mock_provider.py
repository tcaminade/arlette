

class MockProvider:
    async def complete(self, system: str, user: str) -> str:
        return f"[MOCK] {system} :: {user}"