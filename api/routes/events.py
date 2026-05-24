from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps.db import get_db
from services.processings.event_pipeline import EventPipeline
from db.models.event import Event

router = APIRouter()


@router.post("/events")
async def create_event(
    payload: dict[str, Any],
    db: Session = Depends(get_db),
) -> dict[str, Any]:
    pipeline = EventPipeline(db)

    event = Event(**payload)

    result = await pipeline.process_event(event)

    return result