import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...infrastructure.database import base_repository, iov_repository, sqlite

router = APIRouter(
    prefix="/iovs",
    tags=["iovs"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/", response_model=iov_repository.Iov, summary="Create an interval of validity."
)
async def create_iov(
    iov_data: iov_repository.IovCreate,
    db_session: AsyncSession = Depends(sqlite.get_async_session),
) -> iov_repository.Iov:
    """
    Create an interval of validity with the following information:

    - **version**: A user generated label to describe the version. It must be a unique label.
    - **reason**: The reason for creating a new interval of validity.
    """
    iov_repo = base_repository.SqlBaseRepository(iov_repository.Iov, db_session)
    return await iov_repo.create(iov_data.model_dump())


@router.get(
    "/{iov_id}",
    response_model=iov_repository.Iov,
    summary="Fetch an interval of validity using its ID.",
)
async def get_iov(
    iov_id: uuid.UUID,
    db_session: AsyncSession = Depends(sqlite.get_async_session),
) -> iov_repository.Iov:
    """
    Fetch an interval of validity record using its ID.
    """
    iov_repo = base_repository.SqlBaseRepository(iov_repository.Iov, db_session)
    return await iov_repo.get(iov_id)


@router.get(
    "/",
    response_model=List[iov_repository.Iov],
    summary="Fetch all interval of validity records.",
)
async def get_iovs(
    db_session: AsyncSession = Depends(sqlite.get_async_session),
) -> List[iov_repository.Iov]:
    """
    Fetch all interval of validity records.
    """
    iov_repo = base_repository.SqlBaseRepository(iov_repository.Iov, db_session)
    return await iov_repo.get_all()


@router.patch(
    "/{iov_id}",
    response_model=iov_repository.Iov,
    summary="Update an interval of validity record using its ID.",
)
async def update_iov(
    iov_id: uuid.UUID,
    iov_data: iov_repository.IovUpdate,
    db_session: AsyncSession = Depends(sqlite.get_async_session),
) -> iov_repository.Iov:
    """
    Update an interval of validity record, using its ID, with the following information:

    - **(Optional) version**: A user generated label to describe the version. It must be a unique label.
    - **(Optional) reason**: The reason for creating a new interval of validity.
    """
    iov_repo = base_repository.SqlBaseRepository(iov_repository.Iov, db_session)
    return await iov_repo.update(iov_id, iov_data.model_dump(exclude_unset=True))


@router.delete(
    "/{iov_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an interval of validity record using its ID.",
)
async def delete_iov(
    iov_id: uuid.UUID,
    db_session: AsyncSession = Depends(sqlite.get_async_session),
) -> Response:
    """
    Delete an interval of validity record using its ID.
    """
    iov_repo = base_repository.SqlBaseRepository(iov_repository.Iov, db_session)
    deleted = await iov_repo.delete(iov_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Iov not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
