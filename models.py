from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class UsersDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str

    notas: list["NotesDB"] = Relationship(back_populates="owner")


class NotesDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    conteudo: str

    owner_id: int = Field(foreign_key="usersdb.id")
    owner: "UsersDB" = Relationship(back_populates="notas")