import uuid

from sqlmodel import Field, SQLModel


class UUIDMixin(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
