# src/app/core/state.py

_current_flow: dict = {}

def set_current_flow(flow: dict) -> None:
    global _current_flow
    _current_flow = flow

def get_current_flow() -> dict:
    return _current_flow
