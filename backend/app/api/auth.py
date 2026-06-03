from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.app.dependencies.auth import get_current_user
from backend.app.dependencies.database import get_db
from backend.app.models.user import User
from backend.app.services.user import login_user, register_user
from backend.app.schemas.user import (
    TokenResponse, 
    UserCreate, 
    UserLogin, 
    UserResponse,
)


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


@router.post("/login", response_model=TokenResponse)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
):
    token = login_user(
        db,
        UserLogin(
            email=form_data.username,
            password=form_data.password,
        ),
    )
    
    return token


@router.get("/me", response_model=UserResponse)
def get_user(
    user: Annotated[User, Depends(get_current_user)],
):
    return user
    