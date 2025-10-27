from abc import ABC, abstractmethod
from uuid import UUID

from fastapi import APIRouter, Response
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractController(ABC):
    @property
    @abstractmethod
    def router(self) -> APIRouter: ...

    @abstractmethod
    async def create(self, dto: BaseModel, db_session: AsyncSession) -> BaseModel: ...

    @abstractmethod
    async def get(self, id: UUID, db_session: AsyncSession) -> BaseModel: ...

    @abstractmethod
    async def get_all(self, db_session: AsyncSession) -> BaseModel: ...

    @abstractmethod
    async def update(
        self, id: UUID, dto: BaseModel, db_session: AsyncSession
    ) -> BaseModel: ...

    @abstractmethod
    async def delete(self, id: UUID, db_session: AsyncSession) -> Response: ...
