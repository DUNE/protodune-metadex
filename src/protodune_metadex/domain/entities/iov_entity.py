from datetime import datetime

from ..value_objects import CreatedAtVo, IdVo


class IovEntity(IdVo, CreatedAtVo):
    version: str
    reason: str
    updated_at: datetime
