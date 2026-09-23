# API router for regulations
from fastapi import APIRouter
from ..services.regulation_service import RegulationService

router = APIRouter(prefix="/regulations", tags=["regulations"])

regulation_service = RegulationService()

@router.post("/", response_model=dict)
async def create_regulation(regulation: dict):
    return await regulation_service.create_regulation(regulation)

@router.get("/", response_model=list)
async def list_regulations():
    return await regulation_service.list_regulations()
