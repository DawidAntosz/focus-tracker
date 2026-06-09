from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base


class UserSettingsDB(Base):
    __tablename__ = "user_settings"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer, 
        ForeignKey("users.id", ondelete="CASCADE"), 
        unique=True, 
        nullable=False
    )

    work_duration = Column(Integer, default=30) 
    break_duration = Column(Integer, default=5)

    user = relationship("UserDB", back_populates="settings")
