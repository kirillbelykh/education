from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.dependencies.database import get_db
from backend.app.services.user import register_user
from backend.app.schemas.user import UserCreate, UserResponse


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_new_user(
    request: UserCreate,
    db: Annotated[Session, Depends(get_db)],
):
    user = register_user(
        db,
        request,
    )
    
    return user

