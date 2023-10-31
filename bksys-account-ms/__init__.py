"""Initialize client gateway."""

import logging
from functools import lru_cache

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.monitoring import router as monitoring_router
from .settings import AppSettings

log = logging.getLogger(__name__)


@lru_cache()
def settings():
    """Depedency injection for settings."""
    return AppSettings()


# Initialize FastAPI app
app = FastAPI()
log.info("Initializing FastAPI app.")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="https?://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routes
app.include_router(monitoring_router)

__all__ = ["app", "settings"]
