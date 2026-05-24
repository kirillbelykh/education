from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload
from app.database.db import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=100), unique=True)
    created_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    password_hash: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String(length=50), unique=True)
    