from datetime import datetime, timezone

from pydantic import BaseModel, Field


class CreatedAtVo(BaseModel):
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), frozen=True
    )
