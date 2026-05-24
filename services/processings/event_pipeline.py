from typing import Any

from db.models.narrative import Narrative
from db.repositories.event_repository import EventRepository
from services.processings.voices import VoiceEngine


class EventPipeline:
    def __init__(self, db: Any) -> None:
        self.db = db
        self.repo = EventRepository(db)
        self.voices = VoiceEngine()

    async def process_event(self, event: dict[str, Any]) -> dict[str, Any]:
        # --- SAFE ACCESS (API payload dict) ---
        event_id: str | None = event.get("id")
        content: str | None = event.get("content")

        if event_id is None or content is None:
            raise ValueError("Invalid event payload: 'id' and 'content' are required")

        # --- VOICES PIPELINE ---
        ops: str = await self.voices.ops(content)
        audit: str = await self.voices.audit(content)
        arlette: str = await self.voices.arlette(content)

        # --- DOMAIN MODEL ---
        narrative = Narrative(
            event_id=event_id,
            content=(
                f"OPS:\n{ops}\n\n"
                f"AUDIT:\n{audit}\n\n"
                f"ARLETTE:\n{arlette}"
            ),
        )

        # --- PERSISTENCE ---
        # (assume sync repo, donc pas await)
        self.repo.save_narrative(narrative)

        # --- RESPONSE ---
        return {
            "event_id": event_id,
            "narrative": {
                "ops": ops,
                "audit": audit,
                "arlette": arlette,
            },
        }