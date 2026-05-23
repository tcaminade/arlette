from sqlalchemy.orm import Session

from db.repositories.event_repository import EventRepository
from services.llm.client import LLMClient
from db.models.narrative import Narrative

from datetime import datetime, timezone

class EventPipeline:
    def __init__(self, db: Session, llm: LLMClient):
        self.db = db
        self.llm = llm
        self.repo = EventRepository(db)

    async def process_event(
        self,
        *,
        source: str,
        title: str,
        content: str,
        url: str,
    ) -> Narrative:
        event = self.repo.create(
            source=source,
            title=title,
            content=content,
            url=url,
        )

        if event.published_at is None:
            event.published_at = datetime.now(timezone.utc)
            self.db.commit()

        summary = await self.llm.summarize(content)
        arlette = await self.llm.arlette_voice(summary)

        narrative = Narrative(
            event_id=event.id,
            voice="arlette",
            content=arlette,
        )

        self.db.add(narrative)
        self.db.commit()
        self.db.refresh(narrative)

        return narrative