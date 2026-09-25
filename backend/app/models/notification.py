# Placeholder Notification model
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    regulation_id = Column(Integer, ForeignKey("regulations.id"))
    message = Column(String(255))
    read = Column(Boolean, default=False)
    user = relationship("User", backref="notifications")
    regulation = relationship("Regulation", backref="notifications")
