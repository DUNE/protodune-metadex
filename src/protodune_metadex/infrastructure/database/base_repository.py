import uuid
from typing import Any, Dict, Generic, List, Type, TypeVar

from fastapi import HTTPException
from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

T = TypeVar("T", bound=SQLModel)


class SqlBaseRepository(Generic[T]):
    def __init__(self, model: Type[T], async_session: AsyncSession) -> None:
        self.model = model
        self.async_session = async_session

    async def create(self, data: Dict[str, Any], commit=True) -> T:
        try:
            obj = self.model(**data)
            self.async_session.add(obj)
            if commit:
                await self.async_session.commit()
                await self.async_session.refresh(obj)
            return obj
        except Exception as e:
            await self.async_session.rollback()
            raise HTTPException(status_code=400, detail=str(e))

    async def get(self, id: uuid.UUID) -> T:
        obj = await self.async_session.get(self.model, id)
        if not obj:
            raise HTTPException(status_code=404, detail="Item not found")

        return obj

    async def get_all(self) -> List[T]:
        statement = select(self.model)
        result = (await self.async_session.exec(statement)).all()

        return result

    async def update(self, id: uuid.UUID, data: Dict[str, Any], commit=True) -> T:
        obj = await self.async_session.get(self.model, id)
        if not obj:
            raise HTTPException(status_code=404, detail="Item not found")

        for key, value in data.items():
            setattr(obj, key, value)

        if commit:
            await self.async_session.commit()
            await self.async_session.refresh(obj)

        return obj

    async def delete(self, id: uuid.UUID, commit=True) -> bool:
        obj = await self.async_session.get(self.model, id)
        if not obj:
            raise HTTPException(status_code=404, detail="Item not found")

        await self.async_session.delete(obj)
        if commit:
            await self.async_session.commit()
        return True
