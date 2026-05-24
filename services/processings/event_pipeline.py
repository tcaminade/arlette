from typing import Any

from db.models.event import Event
from db.models.narrative import Narrative
from db.repositories.event_repository import EventRepository
from services.processings.voices import VoiceEngine


class EventPipeline:
    def __init__(self, db: Any) -> None:
        self.db = db
        self.repo = EventRepository(db)
        self.voices = VoiceEngine()

    async def process_event(self, event: Event) -> dict[str, Any]:

        self.repo.save_event(event)

        content = event.content

        ops = await self.voices.ops(content)
        audit = await self.voices.audit(content)
        arlette = await self.voices.arlette(content)

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