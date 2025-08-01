from typing import Any, Generator

from sqlalchemy.engine.base import Engine
from sqlmodel import Session, SQLModel, create_engine

connect_args = {"check_same_thread": False}
sqlite_file_name = "dev.protodune-metadex.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
# `echo` is something that should be used for dev / test purposes only
# https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#engine-echo
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_engine_and_tables() -> Engine:
    SQLModel.metadata.create_all(engine)
    return engine


def get_session() -> Generator[Session, Any, None]:
    with Session(engine) as session:
        yield session
