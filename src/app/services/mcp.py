from typing import Any, Dict
import uuid

def mcp_wrap(payload: Any, method: str, request_id: str = None) -> Dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id or str(uuid.uuid4()),
        "method": method,
        "params": { "data": payload }
    }