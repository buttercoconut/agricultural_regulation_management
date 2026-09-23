# Notification model placeholder
from pydantic import BaseModel
class Notification(BaseModel):
    id: int
    user_id: int
    regulation_id: int
    message: str
    read: bool = False
