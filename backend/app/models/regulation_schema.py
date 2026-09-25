# Pydantic schemas for Regulation
from pydantic import BaseModel, Field
from typing import List, Optional

class RegulationBase(BaseModel):
    title: str = Field(..., max_length=255)
    description: Optional[str] = None
    effective_date: Optional[str] = None  # YYYY-MM-DD
    status: Optional[str] = "draft"
    region_ids: Optional[List[int]] = None
    category_ids: Optional[List[int]] = None

class RegulationCreate(RegulationBase):
    pass

class RegulationUpdate(RegulationBase):
    pass

class RegulationInDBBase(RegulationBase):
    id: int

    class Config:
        orm_mode = True

class Regulation(RegulationInDBBase):
    pass

class RegulationList(BaseModel):
    total: int
    items: List[Regulation]
