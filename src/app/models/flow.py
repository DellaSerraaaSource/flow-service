from pydantic import BaseModel
from typing import Any, Dict

class FlowModel(BaseModel):
    flow: Dict[str, Any]
