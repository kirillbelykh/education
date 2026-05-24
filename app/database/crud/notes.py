from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database.models import Note

async def get_notes_from_db(
    user_id: int,
    db: Session, 
    limit: int, 
    offset: int):
    notes = db.query(Note).filter(Note.user_id == user_id).order_by(Note.created_at.desc()).offset(offset).limit(limit).all()
    return notes 