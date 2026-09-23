# Regulation model
from pydantic import BaseModel
from typing import List, Optional

class Regulation(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    region: List[str]
    category: List[str]
    effective_date: str
    status: str
