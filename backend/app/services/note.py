from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.repositories.note import (
    create_note as generate_note,
    delete_note_by_id,
    delete_trashed_note,
    get_note_by_id,
    get_notes,
    get_trashed_notes,
    restore_note_by_id,
    update_note_by_id,
)
from backend.app.schemas.note import NoteCreate, NoteUpdate


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


def get_note(
    db: Session,
    note_id: int,
    user_id: int,
):
    note = get_note_by_id(
        db,
        note_id,
        user_id,
    )
    if note:
        return note 
    
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )
            
    
def delete_note(
    db: Session,
    note_id: int,
    user_id: int,
):
    note_delete = delete_note_by_id(
        db,
        note_id,
        user_id,
    )
    
    if note_delete:
        return note_delete
    
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )
        
def get_notes_from_trash(
    db: Session, 
    user_id: int,
):
    notes = get_trashed_notes(
        db,
        user_id
    )
    
    return notes
    

def restore_note(
    db: Session,
    note_id: int,
    user_id: int,
):
    note = restore_note_by_id(
        db,
        note_id,
        user_id,
    )
    
    if note:
        return note
    
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )
        
    
def update_note(
    note_data: NoteUpdate,
    db: Session,
    note_id: int,
    user_id: int,
):
    note_update = update_note_by_id(
        note_data,
        db,
        note_id,
        user_id,
    )
    
    if note_update:
        return note_update
    
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )
        
        
def hard_delete_note_by_id(
    db: Session,
    note_id: int,
    user_id: int,
):
    note_delete = delete_trashed_note(
        db,
        note_id,
        user_id,
    )
    
    if note_delete:
        return note_delete
    
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )