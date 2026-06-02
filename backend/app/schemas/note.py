from datetime import datetime
from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str
    content_type: str


class NoteUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    content_type: str | None = None


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    content_type: str
    created_at: datetime
    updated_at: datetime
    is_deleted: bool