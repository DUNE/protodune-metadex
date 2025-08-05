from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI

from .infrastructure.database import sqlite
from .interface.api.iov_router import router as iovs_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    engine = sqlite.create_engine_and_tables()
    yield
    # Is this necessary? Or does the context manager closing db sessions handle this?
    engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(iovs_router)
