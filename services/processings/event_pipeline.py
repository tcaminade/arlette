from sqlalchemy.orm import Session

from db.models.narrative import Narrative
from db.repositories.event_repository import EventRepository
from services.llm.client import LLMClient
from services.processings.voices import VoiceEngine


class EventPipeline:
    def __init__(self, db: Session):
        self.db = db
        self.repo = EventRepository(db)

        self.llm = LLMClient()
        self.voices = VoiceEngine(self.llm)

    async def process_event(self, *, source: str, title: str, content: str, url: str):
        event = self.repo.create(
            source=source,
            title=title,
            content=content,
            url=url,
        )

        ops = await self.voices.ops(content)
        audit = await self.voices.audit(content)
        arlette = await self.voices.arlette(content)

        narrative_text = f"""
OPS:
{ops}

AUDIT:
{audit}

ARLETTE:
{arlette}
"""

        narrative = Narrative(
            event_id=event.id,
            voice="multi",
            content=narrative_text,
        )

        self.db.add(narrative)
        self.db.commit()
        self.db.refresh(narrative)

        return {
            "event_id": event.id,
            "narrative": narrative,
            "voices": {
                "ops": ops,
                "audit": audit,
                "arlette": arlette,
            },
        }