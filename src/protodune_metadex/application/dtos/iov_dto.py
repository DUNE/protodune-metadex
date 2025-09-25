from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class IovCreateDto(BaseModel):
    version: str = Field(
        unique=True,
        description="A user generated label to describe the version. It must be a unique label.",
    )
    reason: str = Field(
        description="The reason for creating a new interval of validity"
    )


class IovReadDto(BaseModel):
    id: UUID
    version: str
    reason: str
    created_at: datetime
    updated_at: datetime


class IovUpdateDto(BaseModel):
    version: str | None = Field(
        None,
        unique=True,
        description="A user generated label to describe the version. It must be a unique label.",
    )
    reason: str | None = Field(
        None, description="The reason for creating a new interval of validity"
    )
