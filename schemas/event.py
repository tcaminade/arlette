
from pydantic import BaseModel, Field


# ----------------------------
# INPUT (POST /events)
# ----------------------------
class EventCreate(BaseModel):
    content: str
    source: str | None = None
    title: str | None = None
    url: str | None = None


# ----------------------------
# OUTPUT API (optionnel mais propre)
# ----------------------------
class EventDTO(BaseModel):
    id: str
    content: str
    source: str | None = None
    title: str | None = None
    url: str | None = None


# ----------------------------
# INTERNAL (optionnel pipeline clean)
# ----------------------------
class EventInternal(BaseModel):
    id: str = Field(...)
    content: str
    source: str | None = None
    title: str | None = None
    url: str | None = None