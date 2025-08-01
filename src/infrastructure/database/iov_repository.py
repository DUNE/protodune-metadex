import uuid
from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class Iov(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    version: str = Field(index=True)
    reason: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
    )


class IovCreate(SQLModel):
    version: str
    reason: str


class IovUpdate(SQLModel):
    version: str | None = None
    reason: str | None = None
