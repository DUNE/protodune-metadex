from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
)
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

connect_args = {"check_same_thread": False}
sqlite_file_name = "dev.protodune-metadex.db"
sqlite_url = f"sqlite+aiosqlite:///{sqlite_file_name}"
# `echo` is something that should be used for dev / test purposes only
# https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#engine-echo
async_engine = create_async_engine(
    sqlite_url, connect_args=connect_args, echo=True, future=True
)
async_session = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def create_tables() -> AsyncEngine:
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    return async_engine


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
