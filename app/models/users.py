from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (DateTime, String, Text, Boolean, func, text)
from sqlalchemy.dialects.postgresql import UUID
from uuid6 import uuid7
import uuid

from app.db.base import Base


class User(Base):
    __tablename__ = 'users'

    id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid7
        ) 
    username : Mapped[str] = mapped_column(String(120), nullable=False)
    email : Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    hashed_password : Mapped[str] = mapped_column(Text, nullable=False)
    
    is_active : Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('true'))
    
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now() , nullable=False)

    categories : Mapped[list['Category']] = relationship(back_populates='owner', cascade='all, delete-orphan')
    tasks : Mapped[list['Task']] = relationship(back_populates='user', cascade='all, delete-orphan')
