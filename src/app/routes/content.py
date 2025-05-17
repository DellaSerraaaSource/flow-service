from fastapi import APIRouter, HTTPException, Query
from app.services.extractor import extract_actions
from app.services.mcp import mcp_wrap
from app.core.state import get_current_flow

router = APIRouter(prefix="/content", tags=["content"])

@router.get("/{action}")
async def get_content_action(
    action: str,
    mcp: bool = Query(False, description="Se true, embala a resposta em MCP"),
    id: str = Query(None, description="ID de requisição para o protocolo MCP")
):
    flow = get_current_flow()
    result = extract_actions(flow, custom_action_key="$contentActions")
    if action not in result:
        raise HTTPException(status_code=404, detail=f"Ação '{action}' não encontrada")
    payload = result[action]
    return mcp_wrap(payload, method=f"flow.content.{action}", request_id=id) if mcp else payload