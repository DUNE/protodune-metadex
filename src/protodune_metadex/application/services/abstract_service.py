from abc import ABC, abstractmethod
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractService(ABC):
    @abstractmethod
    async def __call__(
        self, db_session: AsyncSession, dto: BaseModel | None, id: UUID | None
    ) -> BaseModel: ...
