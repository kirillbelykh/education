from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.repositories.note import (
    create_note as generate_note, 
    get_notes,
    )
from backend.app.schemas.note import NoteCreate


def create_new_note(
    db: Session,
    note_data: NoteCreate,
    user_id: int,
):
    try:
        note = generate_note(
            db,
            note_data,
            user_id,
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unable to create note",
        )
        
    return note

def get_all_notes(
    db: Session,
    user_id: int,
):
    notes = get_notes(
        db,
        user_id,
    )
    
    return notes 