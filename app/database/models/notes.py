from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload
from app.database.db import Base
from .users import User
from datetime import datetime


class Note(Base):
    __tablename__ = 'notes'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    title: Mapped[str | None] = mapped_column(String(length=50), nullable=True)
    text: Mapped[str | None] = mapped_column(Text(length=5000), nullable=True)
    created_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey(User.id))
    created_by: Mapped[str | None] = relationship("Note", back_populates="users")
    
    
