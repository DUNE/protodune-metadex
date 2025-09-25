from sqlalchemy.ext.asyncio import AsyncSession

from ....infrastructure.database.models import Iov
from ....infrastructure.database.repositories import SqlRepository
from ...dtos import IovCreateDto, IovReadDto
from .. import AbstractService


class CreateIovService(AbstractService):
    async def __call__(self, db_session: AsyncSession, dto: IovCreateDto) -> IovReadDto:
        iov_repo = SqlRepository(Iov, db_session)
        result: Iov = await iov_repo.create(dto.model_dump())

        return IovReadDto(**result.model_dump())
