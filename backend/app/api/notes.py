from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.dependencies.auth import get_current_user
from backend.app.dependencies.database import get_db
from backend.app.models.user import User
from backend.app.schemas.note import NoteCreate, NoteResponse, NoteUpdate
from backend.app.services.note import (
    create_new_note,
    delete_note,
    get_all_notes,
    get_note,
    get_notes_from_trash,
    hard_delete_note_by_id,
    restore_note,
    update_note,
)

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(
    request: NoteCreate,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    note = create_new_note(
        db,
        request,
        user_id=current_user.id,
    )
    
    return note


@router.get("", response_model=list[NoteResponse])
def get_notes(
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    notes = get_all_notes(
        db,
        user_id=current_user.id,
    )
    
    return notes
    

@router.get("/trash", response_model=list[NoteResponse])
def get_trashed_notes(
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    trashed_notes = get_notes_from_trash(
        db,
        user_id=current_user.id,
    )
    
    return trashed_notes
    
    
@router.get("/{note_id}", response_model=NoteResponse)
def get_note_by_id(
    db: Annotated[Session, Depends(get_db)],
    note_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
):
    note = get_note(
        db,
        note_id,
        user_id=current_user.id,
    )
    
    return note


@router.delete("/{note_id}", response_model=NoteResponse)
def delete_note_by_id(
    db: Annotated[Session, Depends(get_db)],
    note_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
):
    note_delete = delete_note(
        db,
        note_id,
        user_id=current_user.id,
    )
    
    return note_delete


@router.patch("/{note_id}/restore", response_model=NoteResponse)
def restore_note_from_trash(
    db: Annotated[Session, Depends(get_db)],
    note_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
):
    note = restore_note(
        db,
        note_id,
        user_id=current_user.id,
    )
    
    return note


@router.patch("/{note_id}", response_model=NoteResponse)
def update_note_by_id(
    request: NoteUpdate,
    db: Annotated[Session, Depends(get_db)],
    note_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
):
    note_update = update_note(
        request,
        db,
        note_id,
        user_id=current_user.id,
    )
    
    return note_update


@router.delete("/trash/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note_from_trash(
    db: Annotated[Session, Depends(get_db)],
    note_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
):
    hard_delete_note_by_id(
        db,
        note_id,
        user_id=current_user.id,
    )
    

        