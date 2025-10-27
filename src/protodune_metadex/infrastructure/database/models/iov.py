from sqlmodel import Field

from ..mixins import CreatedAtMixin, UpdatedAtMixin, UUIDMixin


class Iov(CreatedAtMixin, UpdatedAtMixin, UUIDMixin, table=True):
    version: str = Field(
        index=True,
        unique=True,
        description="A user generated label to describe the version. It must be a unique label.",
    )
    reason: str = Field(
        description="The reason for creating a new interval of validity"
    )
