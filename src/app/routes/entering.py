from fastapi import APIRouter, HTTPException
from app.services.extractor import extract_actions
from app.core.state import get_current_flow

router = APIRouter(prefix="/entering", tags=["entering"])

@router.get("/{action}")
async def get_entering_action(action: str):
    flow = get_current_flow()
    result = extract_actions(flow, custom_action_key="$enteringCustomActions")
    if action not in result:
        raise HTTPException(status_code=404, detail=f"Ação '{action}' não encontrada")
    return result[action]
