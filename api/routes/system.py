from fastapi import APIRouter

from core.config import get_settings

router = APIRouter(prefix="/system", tags=["system"])


@router.get("/info")
async def info() -> dict[str, str]:
    settings = get_settings()

    return {
        "app_name": settings.app_name,
    }