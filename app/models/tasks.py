from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (Identity, DateTime, Index, Integer, String, Text,func, ForeignKey, CheckConstraint)
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class Task(Base):
    __tablename__ = 'tasks'

    id : Mapped[int] = mapped_column(Identity(), primary_key=True)
    user_id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )
    category_id : Mapped[int] = mapped_column(
        ForeignKey('categories.id', ondelete='CASCADE'),
        nullable=False
    )

    title : Mapped[str] = mapped_column(String(120), nullable=False)
    description : Mapped[str | None] = mapped_column(Text, default=None)

    # TO:DO
    status : Mapped[str] = mapped_column(String(16), nullable=False, default='todo')
    # Приоритетность от 1 до 5
    priority : Mapped[int] = mapped_column(Integer, nullable=False, default=2)
    
    due_date : Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    completed_at : Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now() , nullable=False)

    user : Mapped['User'] = relationship(back_populates='tasks')
    category : Mapped['Category'] = relationship(back_populates='tasks')

    __table_args__ = (
        CheckConstraint("status IN ('todo', 'in_progress', 'done')", name='chk_status' ),
        CheckConstraint('priority BETWEEN 1 AND 5'),
        Index('idx_tasks_user_id', 'user_id'),
        Index('idx_tasks_category_id', 'category_id'),
        Index('idx_tasks_status', 'status'),
        Index('idx_tasks_due_date', 'due_date')
    )
