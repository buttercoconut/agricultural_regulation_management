# Notification service placeholder
from typing import List
from sqlalchemy.orm import Session
from . import notification as notification_models

class NotificationService:
    def __init__(self, db: Session):
        self.db = db
    def create_notification(self, user_id: int, regulation_id: int, message: str):
        notif = notification_models.Notification(user_id=user_id, regulation_id=regulation_id, message=message)
        self.db.add(notif)
        self.db.commit()
        self.db.refresh(notif)
        return notif
