from typing import Dict, List

def extract_actions(flow: dict, custom_action_key: str) -> Dict[str, List[dict]]:
    tipos = [
        "SetVariable", "MergeContact", "TrackEvent",
        "ExecuteScript", "ProcessHttp", "Redirect"
    ]
    return {
        tipo: [
            {
                "bloco_id": bloco_id,
                "titulo_bloco": bloco.get("$title", ""),
                **acao
            }
            for bloco_id, bloco in flow.get("flow", {}).items()
            for acao in bloco.get(custom_action_key, [])
            if acao.get("type") == tipo
        ]
        for tipo in tipos
    }