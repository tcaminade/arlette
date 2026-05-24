from uuid import uuid4

from pydantic import BaseModel, Field


class EventCreate(BaseModel):
    content: str
    source: str | None = None
    title: str | None = None
    url: str | None = None


class EventDTO(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    content: str
    source: str | None = None
    title: str | None = None
    url: str | None = None