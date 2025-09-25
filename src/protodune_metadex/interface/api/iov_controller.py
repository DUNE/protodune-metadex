import uuid

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...application.dtos import IovCreateDto, IovReadDto, IovUpdateDto
from ...application.services.iov import (
    CreateIovService,
    DeleteIovService,
    GetAllIovService,
    GetIovService,
    UpdateIovService,
)
from ...infrastructure.database import sqlite
from . import AbstractController


class IovController(AbstractController):
    router = APIRouter(
        prefix="/iovs",
        tags=["iovs"],
        responses={404: {"description": "Not found"}},
    )

    @router.post(
        "/",
        summary="Create an interval of validity record.",
    )
    async def create(
        dto: IovCreateDto,
        db_session: AsyncSession = Depends(sqlite.get_async_session),
        service: CreateIovService = Depends(CreateIovService),
    ) -> IovReadDto:
        """
        Create an interval of validity with the following information:

        - **version**: A user generated label to describe the version. It must be a unique label.
        - **reason**: The reason for creating a new interval of validity.
        """
        return await service(db_session, dto)

    @router.get(
        "/{iov_id}",
        summary="Fetch an interval of validity using its ID.",
    )
    async def get(
        id: uuid.UUID,
        db_session: AsyncSession = Depends(sqlite.get_async_session),
        service: GetIovService = Depends(GetIovService),
    ) -> IovReadDto:
        """
        Fetch an interval of validity record using its ID.
        """
        return await service(db_session, id)

    @router.get(
        "/",
        summary="Fetch all interval of validity records.",
    )
    async def get_all(
        db_session: AsyncSession = Depends(sqlite.get_async_session),
        service: GetAllIovService = Depends(GetAllIovService),
    ) -> list[IovReadDto]:
        """
        Fetch all interval of validity records.
        """
        return await service(db_session)

    @router.patch(
        "/{iov_id}",
        summary="Update an interval of validity record using its ID.",
    )
    async def update(
        id: uuid.UUID,
        dto: IovUpdateDto,
        db_session: AsyncSession = Depends(sqlite.get_async_session),
        service: UpdateIovService = Depends(UpdateIovService),
    ) -> IovReadDto:
        """
        Update an interval of validity record, using its ID, with the following information:

        - **(Optional) version**: A user generated label to describe the version. It must be a unique label.
        - **(Optional) reason**: The reason for creating a new interval of validity.
        """
        return await service(db_session, dto, id)

    @router.delete(
        "/{iov_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete an interval of validity record using its ID.",
    )
    async def delete(
        id: uuid.UUID,
        db_session: AsyncSession = Depends(sqlite.get_async_session),
        service: DeleteIovService = Depends(DeleteIovService),
    ) -> Response:
        """
        Delete an interval of validity record using its ID.
        """
        deleted = await service(db_session, id)

        if not deleted:
            raise HTTPException(status_code=404, detail="Iov not found")

        return Response(status_code=status.HTTP_204_NO_CONTENT)
