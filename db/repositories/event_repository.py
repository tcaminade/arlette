from sqlalchemy.orm import Session

from db.models.event import Event
from db.models.narrative import Narrative


class EventRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def save_event(self, event: Event) -> None:
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)

    def save_narrative(self, narrative: Narrative) -> None:
        self.db.add(narrative)
        self.db.commit()
        self.db.refresh(narrative)