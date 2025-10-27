from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI

from .infrastructure.database import sqlite
from .interface.api import IovController


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    async_engine = await sqlite.create_tables()
    yield
    await async_engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(IovController().router)
