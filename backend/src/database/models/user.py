from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from ..base import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)

    created_at = Column(
        DateTime, 
        default=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )

    settings = relationship("UserSettingsDB", back_populates="user", uselist=False, cascade="all, delete-orphan")
    tasks = relationship("TaskDB", back_populates="owner", cascade="all, delete-orphan")
