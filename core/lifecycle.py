from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI

from core.config import get_settings
from core.logging import configure_logging

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    configure_logging()

    settings = get_settings()

    logger.info(
        "application_starting",
        app_name=settings.app_name,
        debug=settings.debug,
    )

    yield

    logger.info("application_stopping")