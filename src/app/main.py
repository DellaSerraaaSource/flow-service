from fastapi import FastAPI
from app.routes.import_flow import router as import_flow_router
from app.routes.leaving    import router as leaving_router
from app.routes.entering   import router as entering_router
from app.routes.content    import router as content_router

app = FastAPI(title="Flow-Service", version="0.1.0")

app.include_router(import_flow_router)
app.include_router(leaving_router)
app.include_router(entering_router)
app.include_router(content_router)