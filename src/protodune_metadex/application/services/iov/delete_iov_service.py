from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from ....infrastructure.database.models import Iov
from ....infrastructure.database.repositories import SqlRepository
from .. import AbstractService


class DeleteIovService(AbstractService):
    async def __call__(self, db_session: AsyncSession, id: UUID) -> bool:
        iov_repo = SqlRepository(Iov, db_session)
        return await iov_repo.delete(id)
