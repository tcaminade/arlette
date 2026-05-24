from fastapi import FastAPI

from api.routes import router as api_router
from core.lifecycle import lifespan


app = FastAPI(lifespan=lifespan)

app.include_router(api_router)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}