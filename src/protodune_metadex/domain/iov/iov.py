from pydantic import BaseModel


class Iov(BaseModel):
    id: int | None = None
    version: str
    reason: str
