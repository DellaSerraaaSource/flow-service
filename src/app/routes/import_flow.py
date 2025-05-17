from fastapi import APIRouter
from app.models.flow import FlowModel
from app.core.state import set_current_flow

router = APIRouter(prefix="/import", tags=["import"])

@router.post("", status_code=201)
async def import_flow(flow: FlowModel):
    set_current_flow(flow.dict())
    return {"detail": "Fluxo importado com sucesso"}