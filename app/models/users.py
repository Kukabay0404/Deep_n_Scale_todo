from datetime import datetime
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (DateTime, String, Boolean, func, text)


from app.db.base import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'users'

    username : Mapped[str] = mapped_column(String(120), nullable=False)
    
    is_active : Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('true'))
    
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now() , nullable=False)

    categories : Mapped[list['Category']] = relationship(back_populates='owner', cascade='all, delete-orphan')
    tasks : Mapped[list['Task']] = relationship(back_populates='user', cascade='all, delete-orphan')
