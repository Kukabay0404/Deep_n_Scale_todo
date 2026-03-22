from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (Identity, DateTime, Index, String,func, ForeignKey, UniqueConstraint)
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base

class Category(Base):
    __tablename__ = 'categories'

    id : Mapped[int] = mapped_column(Identity(), primary_key=True)
    category_name : Mapped[str] = mapped_column(String(120), nullable=False)    
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    owner_id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False 
    )

    owner : Mapped['User'] = relationship(back_populates='categories')
    tasks : Mapped[list['Task']] = relationship(back_populates='category', cascade='all, delete-orphan')

    __table_args__ = (
        UniqueConstraint('category_name', 'owner_id', name='uq_category_name_owner_id'),
        Index('idx_categories_owner_id', 'owner_id')
    )

    
