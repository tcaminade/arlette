from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.models.event import Event as EventModel
from db.session import get_db
from schemas.event import EventCreate
from services.processings.event_pipeline import EventPipeline

router = APIRouter()


@router.post("/events")
async def create_event(
    payload: EventCreate,
    db: Session = Depends(get_db),
) -> dict[str, Any]:

    # 1. Construire l'entité DB (SQLAlchemy)
    event = EventModel(
        content=payload.content,
        source=payload.source,
        title=payload.title,
        url=payload.url,
    )

    # 2. Pipeline
    pipeline = EventPipeline(db)

    result = await pipeline.process_event(event)

    return result