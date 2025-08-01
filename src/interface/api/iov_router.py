from fastapi import APIRouter, Depends
from sqlmodel import Session

from ...infrastructure.database import base_repository, iov_repository, sqlite

router = APIRouter(
    prefix="/iovs",
    tags=["iovs"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", summary="Create an interval of validity")
async def create_iov(
    iov_data: iov_repository.IovCreate,
    db_session: Session = Depends(sqlite.get_session),
) -> iov_repository.Iov:
    """
    Create an interval of validity with the following information:

    - **version**: A user generated label to describe the version.
    - **reason**: The reason for creating a new interval of validity.
    """
    iov_repo = base_repository.BaseRepository(iov_repository.Iov, db_session)
    return iov_repo.create(iov_data.model_dump())
