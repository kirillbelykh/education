from fastapi import Depends, Query
from fastapi.routing import APIRouter
from app.database import get_db, get_notes_from_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/notes", tags=["notes"])

@router.get("/")
async def get_notes(
    user_id: int,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    notes = await get_notes_from_db(
        user_id=user_id,
        db=db,
        limit=limit,
        offset=offset,
    )

    return notes 


    


 


