# User service placeholder
from typing import Optional
from sqlalchemy.orm import Session
from . import user as user_models

class UserService:
    def __init__(self, db: Session):
        self.db = db
    def get_user(self, user_id: int) -> Optional[user_models.User]:
        return self.db.query(user_models.User).filter(user_models.User.id == user_id).first()
