from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class UpdatedAtMixin(SQLModel):
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)},
    )
