from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps.db import get_db
from services.processings.event_pipeline import EventPipeline

router = APIRouter()


@router.post("/events")
async def create_event(
    payload: dict[str, Any],
    db: Session = Depends(get_db),
) -> dict[str, Any]:
    """
    Create an event and run it through the Arlette processing pipeline.

    Returns structured narrative output (OPS / AUDIT / ARLETTE).
    """
    pipeline = EventPipeline(db)

    result: dict[str, Any] = await pipeline.process_event(payload)

    return result