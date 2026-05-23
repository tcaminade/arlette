from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class Narrative(Base):
    __tablename__ = "narratives"

    id: Mapped[int] = mapped_column(primary_key=True)

    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id"),
    )

    voice: Mapped[str] = mapped_column(String(100))

    content: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )