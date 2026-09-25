# Service layer for Regulation
from typing import List, Optional
from sqlalchemy.orm import Session
from . import regulation as regulation_models
from . import regulation_schema

class RegulationService:
    def __init__(self, db: Session):
        self.db = db

    def create_regulation(self, reg_in: regulation_schema.RegulationCreate) -> regulation_models.Regulation:
        # Core logic: create Regulation and associate regions/categories
        reg = regulation_models.Regulation(
            title=reg_in.title,
            description=reg_in.description,
            effective_date=reg_in.effective_date,
            status=reg_in.status,
        )
        # Handle many-to-many associations
        if reg_in.region_ids:
            regions = self.db.query(regulation_models.Region).filter(regulation_models.Region.id.in_(reg_in.region_ids)).all()
            reg.regions = regions
        if reg_in.category_ids:
            categories = self.db.query(regulation_models.Category).filter(regulation_models.Category.id.in_(reg_in.category_ids)).all()
            reg.categories = categories
        self.db.add(reg)
        self.db.commit()
        self.db.refresh(reg)
        return reg

    def get_regulation(self, reg_id: int) -> Optional[regulation_models.Regulation]:
        return self.db.query(regulation_models.Regulation).filter(regulation_models.Regulation.id == reg_id).first()

    def list_regulations(self, skip: int = 0, limit: int = 10) -> List[regulation_models.Regulation]:
        return self.db.query(regulation_models.Regulation).offset(skip).limit(limit).all()

    def delete_regulation(self, reg_id: int) -> None:
        reg = self.get_regulation(reg_id)
        if reg:
            self.db.delete(reg)
            self.db.commit()
