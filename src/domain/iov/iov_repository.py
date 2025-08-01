from abc import ABC, abstractmethod

from iov import Iov


class IovRepository(ABC):
    @abstractmethod
    async def save(self, iov: Iov) -> None:
        pass
