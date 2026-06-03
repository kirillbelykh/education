from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.models import Note
from backend.app.schemas.note import NoteCreate, NoteUpdate


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
        select(Note).where(
            Note.user_id == user_id, 
            Note.is_deleted.is_(False),
        )
    ).all()
    
    return notes 
    

def delete_note_by_id(
    db: Session,
    note_id: int,
    user_id: int,
):
    note = _get_active_note_by_id(
        db,
        note_id,
        user_id,
    )
    
    if note:
        note.is_deleted = True 
        db.commit()
        db.refresh(note)
        return note 
    
    return None 
    

def get_trashed_notes(
    db: Session,
    user_id: int,
):
    notes_from_trash = db.scalars(
        select(Note).where(Note.user_id == user_id, Note.is_deleted.is_(True))
    ).all()
    
    return notes_from_trash


def restore_note_by_id(
    db: Session,
    note_id: int,
    user_id: int,
):
    note = _get_trashed_note_by_id(
        db,
        note_id,
        user_id,
    )
    
    if note:
        note.is_deleted = False
        db.commit()
        db.refresh(note)
        return note
    
    return None 


def update_note_by_id(
    note_data: NoteUpdate,
    db: Session,
    note_id: int,
    user_id: int,
):
    note = _get_active_note_by_id(
        db,
        note_id,
        user_id,
    ) 
    update_data = note_data.model_dump(exclude_unset=True)
    
    for f_name, f_value in update_data.items():
        setattr(note, f_name, f_value)
        
    db.commit()
    db.refresh(note)
    
    return note 

    
def delete_trashed_note(
    db: Session,
    note_id: int,
    user_id: int,
):
    note = _get_trashed_note_by_id(
        db,
        note_id,
        user_id,
    )
    
    if note is None:
        return None
    
    db.delete(note)
    db.commit()
    
    return True 


def _get_active_note_by_id(
    db: Session,
    note_id: int,
    user_id: int,
):
    note = db.scalars(
        select(Note).where(
            Note.id == note_id,
            Note.user_id == user_id,
            Note.is_deleted.is_(False))
            ).first()
    
    return note


def _get_trashed_note_by_id(
    db: Session,
    note_id: int,
    user_id: int,
):
    note = db.scalars(
        select(Note).where(
            Note.id == note_id,
            Note.user_id == user_id,
            Note.is_deleted.is_(True))
            ).first()
    
    return note


def get_note_by_id(
    db: Session,
    note_id: int,
    user_id: int,
):
    return _get_active_note_by_id(
        db,
        note_id,
        user_id,
    )