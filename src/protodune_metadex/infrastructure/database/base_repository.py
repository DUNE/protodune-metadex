import uuid
from typing import Any, Dict, Generic, List, Type, TypeVar

from fastapi import HTTPException
from sqlmodel import Session, SQLModel, select

T = TypeVar("T", bound=SQLModel)


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], session: Session) -> None:
        self.model = model
        self.session = session

    def create(self, data: Dict[str, Any], commit=True) -> T:
        try:
            obj = self.model(**data)
            self.session.add(obj)
            if commit:
                self.session.commit()
                self.session.refresh(obj)
            return obj
        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=400, detail=str(e))

    def get(self, id: uuid.UUID) -> T:
        return self.session.get(self.model, id)

    def get_all(self) -> List[T]:
        statement = select(self.model)
        return self.session.exec(statement).all()

    def update(self, id: uuid.UUID, data: Dict[str, Any], commit=True) -> T:
        obj = self.session.get(self.model, id)
        if not obj:
            raise HTTPException(status_code=404, detail="Item not found")

        for key, value in data.items():
            setattr(obj, key, value)

        if commit:
            self.session.commit()
            self.session.refresh(obj)

        return obj

    def delete(self, id: uuid.UUID, commit=True) -> bool:
        obj = self.session.get(self.model, id)
        if not obj:
            raise HTTPException(status_code=404, detail="Item not found")

        self.session.delete(obj)
        if commit:
            self.session.commit()
        return True
