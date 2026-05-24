from fastapi import APIRouter
from api.routes.events import router as events_router
from api.routes.system import router as system_router

router = APIRouter()

router.include_router(events_router)
router.include_router(system_router)