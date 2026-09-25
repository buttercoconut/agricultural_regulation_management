# API router for Regulation
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..services import regulation_service
from ..models import regulation_schema, regulation as regulation_models
from ..models import __init__ as models_init

router = APIRouter()

# Dependency to get DB session

def get_db():
    db = models_init.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=regulation_schema.Regulation, status_code=status.HTTP_201_CREATED)
def create_regulation(reg_in: regulation_schema.RegulationCreate, db: Session = Depends(get_db)):
    service = regulation_service.RegulationService(db)
    try:
        reg = service.create_regulation(reg_in)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return reg

@router.get("/{reg_id}", response_model=regulation_schema.Regulation)
def read_regulation(reg_id: int, db: Session = Depends(get_db)):
    service = regulation_service.RegulationService(db)
    reg = service.get_regulation(reg_id)
    if not reg:
        raise HTTPException(status_code=404, detail="Regulation not found")
    return reg

@router.get("/", response_model=regulation_schema.RegulationList)
def list_regulations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = regulation_service.RegulationService(db)
    regs = service.list_regulations(skip=skip, limit=limit)
    return regulation_schema.RegulationList(total=len(regs), items=regs)

@router.delete("/{reg_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_regulation(reg_id: int, db: Session = Depends(get_db)):
    service = regulation_service.RegulationService(db)
    reg = service.get_regulation(reg_id)
    if not reg:
        raise HTTPException(status_code=404, detail="Regulation not found")
    service.delete_regulation(reg_id)
    return None
