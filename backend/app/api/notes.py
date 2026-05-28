from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.dependencies.database import get_db
from backend.app.schemas.note import NoteCreate, NoteResponse
from backend.app.services.note import create_new_note


router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(
    request: NoteCreate,
    db: Annotated[Session, Depends(get_db)],
):
    note = create_new_note(
        db,
        request,
        user_id=3,
    )
    
    return note
    
