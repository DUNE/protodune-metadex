from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from ....infrastructure.database.models import Iov
from ....infrastructure.database.repositories import SqlRepository
from ...dtos import IovReadDto, IovUpdateDto
from .. import AbstractService


class UpdateIovService(AbstractService):
    async def __call__(
        self, db_session: AsyncSession, dto: IovUpdateDto, id: UUID
    ) -> IovReadDto:
        iov_repo = SqlRepository(Iov, db_session)
        result: Iov = await iov_repo.update(id, dto.model_dump(exclude_unset=True))

        return IovReadDto(**result.model_dump())
