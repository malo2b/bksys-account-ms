"""Monitoring routes."""

import logging
from fastapi import APIRouter, Response
from starlette import status

log = logging.getLogger(__name__)

router = APIRouter()


@router.get("/service-status", tags=["monitoring"])
async def service_status():
    """Return service status."""
    log.info("Service status requested.")
    return Response(status_code=status.HTTP_200_OK, content="OK")

__all__ = ["router"]
