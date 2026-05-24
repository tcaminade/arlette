from datetime import UTC, datetime

from sqlalchemy.orm import Session

from db.models.event import Event
from db.models.narrative import Narrative


class EventRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, *, source: str, title: str, content: str, url: str) -> Event:
        event = Event(
            source=source,
            title=title,
            content=content,
            url=url,
            published_at=datetime.now(UTC),
        )

        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)

        return event

    def save_narrative(self, narrative: Narrative) -> None:
        self.db.add(narrative)
        self.db.commit()
        self.db.refresh(narrative)