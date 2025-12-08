
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from typing import AsyncGenerator
from .config import settings


class Base(AsyncAttrs, DeclarativeBase):
    pass


engine = create_async_engine(settings.DATABASE_URL, echo=False)


AsyncSessionLocal = async_sessionmaker(
    engine, autocommit=False, autoflush=False, expire_on_commit=False
)


async def get_async_db() -> AsyncGenerator[sessionmaker, None]:
    """
    Async session dependency injection generator.
    When an endpoint requests this dependency, 
    FastAPI automatically opens a session,
    passes it to the function, and then closes 
    after the request is completed.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise


async def init_db():
    """Create DB tables"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
