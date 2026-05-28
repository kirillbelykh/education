from sqlalchemy.orm import Session

from backend.app.models.note import Note
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

    db.add(note)
    db.commit()
    db.refresh(note)
    return note 