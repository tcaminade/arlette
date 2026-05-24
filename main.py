from fastapi import FastAPI

from api.routes import router as api_router
from core.lifecycle import lifespan
from db.base import Base

# IMPORTANT:
# importer les modèles avant create_all
from db.session import engine

app = FastAPI(
    title="Arlette",
    lifespan=lifespan,
)

Base.metadata.create_all(bind=engine)

app.include_router(api_router)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}