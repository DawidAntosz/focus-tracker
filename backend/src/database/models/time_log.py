from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from ..base import Base


class TimeLogDB(Base):
    __tablename__ = "time_logs"

    id = Column(Integer, primary_key=True)
    task_id = Column(
        Integer, 
        ForeignKey("tasks.id", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )

    duration_seconds = Column(Integer, nullable=False)

    end_time = Column(
        DateTime, 
        default=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )

    task = relationship("TaskDB", back_populates="time_logs")
