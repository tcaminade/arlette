from datetime import datetime, timezone

from sqlalchemy.orm import Session

from db.models.event import Event


class EventRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, *, source: str, title: str, content: str, url: str) -> Event:
        event = Event(
            source=source,
            title=title,
            content=content,
            url=url,
            published_at=datetime.now(timezone.utc),
        )

        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)

        return event