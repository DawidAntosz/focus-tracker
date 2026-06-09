from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from src.common import Status
from ..base import Base


class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    title = Column(String(200), nullable=False)
    description = Column(String(500))

    status = Column(
        SQLEnum(Status, name="task_status"), 
        default=Status.NOT_STARTED, 
        nullable=False
    )

    created_at = Column(
        DateTime, 
        default=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )

    owner = relationship("UserDB", back_populates="tasks")
    time_logs = relationship("TimeLogDB", back_populates="task", cascade="all, delete-orphan")
