from datetime import datetime
from fastapi import APIRouter, status
from backend.app.schemas.note import NoteCreate, NoteResponse


router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(request: NoteCreate):
    now = datetime.now()
    return {
        "title": request.title,
        "content": request.content,
        "content_type": request.content_type,
        "id": 1,
        "created_at": now,
        "updated_at": now,
        "is_deleted": False
    }