from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.models import Note
from backend.app.schemas.note import NoteCreate


def create_note(
    db: Session,
    note_data: NoteCreate,
    user_id: int,
):
    note = Note(
        user_id=user_id,
        title=note_data.title,
        content=note_data.content,
        content_type=note_data.content_type,
    )
    try:
        db.add(note)
        db.commit()
        db.refresh(note)
        return note
    
    except IntegrityError:
        db.rollback()
        raise
    
    
def get_notes(
    db: Session,
    user_id: int,
):
    notes = db.scalars(
        select(Note).where(Note.user_id == user_id, Note.is_deleted.is_(False))
            ).all()
    
    return notes 
    