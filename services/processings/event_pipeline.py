from typing import Any

from db.models.narrative import Narrative
from db.repositories.event_repository import EventRepository
from services.processings.voices import VoiceEngine
from db.models.event import Event


class EventPipeline:
    def __init__(self, db: Any) -> None:
        self.db = db
        self.repo = EventRepository(db)
        self.voices = VoiceEngine()

    async def process_event(self, event: Event) -> dict[str, Any]:
        # validation stricte (fail fast)
        if not event.id or not event.content:
            raise ValueError("Invalid event payload: 'id' and 'content' are required")

        content: str = event.content

        ops: str = await self.voices.ops(content)
        audit: str = await self.voices.audit(content)
        arlette: str = await self.voices.arlette(content)

        narrative = Narrative(
            event_id=event.id,
            content=f"OPS:\n{ops}\n\nAUDIT:\n{audit}\n\nARLETTE:\n{arlette}",
        )

        self.repo.save_narrative(narrative)

        return {
            "event_id": event.id,
            "narrative": {
                "ops": ops,
                "audit": audit,
                "arlette": arlette,
            },
        }