from sqlalchemy.ext.asyncio import AsyncSession

from ....infrastructure.database.models import Iov
from ....infrastructure.database.repositories import SqlRepository
from ...dtos import IovReadDto
from .. import AbstractService


class GetAllIovService(AbstractService):
    async def __call__(self, db_session: AsyncSession) -> list[IovReadDto]:
        iov_repo = SqlRepository(Iov, db_session)
        result: list[Iov] = await iov_repo.get_all()

        return [IovReadDto(**iov.model_dump()) for iov in result]
