from sqlalchemy.orm import Session

from backend.app.schemas.note import NoteCreate
from backend.app.repositories.note import create_note 


def create_new_note(
    db: Session,
    note_data: NoteCreate,
    user_id: int,
):
    note = create_note(
        db,
        note_data,
        user_id,
    )
    
    return note

