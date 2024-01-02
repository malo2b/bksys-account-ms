from fastapi import Request
from .settings import app_settings


from aiomysql import create_pool
from aiomysql.connection import Connection
from aiomysql.utils import _PoolContextManager as PoolContextManager


async def initialize_pool() -> PoolContextManager:
    """Initialize database connection pool."""
    return await create_pool(
        host=app_settings.DB_HOST,
        port=app_settings.DB_PORT,
        user=app_settings.DB_USER,
        password=app_settings.DB_PASSWORD,
        db=app_settings.DB_NAME,
        autocommit=True,
    )


async def get_db(request: Request) -> Connection:
    """Dependency for getting a database connection."""
    async with request.app.state.pool.acquire() as conn:
        yield conn


__all__ = ["get_db", "initialize_pool"]
