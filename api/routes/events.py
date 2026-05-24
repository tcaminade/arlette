from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps.db import get_db
from services.processings.event_pipeline import EventPipeline

router = APIRouter(prefix="/events", tags=["events"])


@router.post("")
async def create_event(
    payload: dict,
    db: Session = Depends(get_db),
):
    pipeline = EventPipeline(db)

    result = await pipeline.process_event(
        source=payload["source"],
        title=payload["title"],
        content=payload["content"],
        url=payload["url"],
    )

    return result