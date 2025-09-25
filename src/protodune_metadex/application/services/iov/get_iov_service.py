from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from ....infrastructure.database.models import Iov
from ....infrastructure.database.repositories import SqlRepository
from ...dtos import IovReadDto
from .. import AbstractService


class GetIovService(AbstractService):
    async def __call__(self, db_session: AsyncSession, id: UUID) -> IovReadDto:
        iov_repo = SqlRepository(Iov, db_session)
        result: Iov = await iov_repo.get(id)

        return IovReadDto(**result.model_dump())
