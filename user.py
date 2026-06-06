from models import UsersDB
from depedencies import get_session
from schemas import UserCreate 

from fastapi import APIRouter, Depends
from sqlmodel import Session

router = APIRouter()

@router.post("/create_user")
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session)
):
    novo_usuario = UsersDB(
        nome=user.nome,
        email=user.email
    )

    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)

    return novo_usuario

@router.get("/_users")
def listar_usuarios(
    session: Session = Depends(get_session)
):
    usuarios = session.exec(
        select(UsersDB)
    ).all()

    return usuarios    

@router.get("/find_user/{user_id}")
def buscar_usuario(
    user_id: int,
    session: Session = Depends(get_session)
):
    usuario = session.get(UsersDB, user_id)

    if usuario is None:
        return {"erro": "Usuário não encontrado"}

    return usuario
    
@router.delete("/user_delete/{user_id}")
def deletar_usuario(
    user_id: int,
    session: Session = Depends(get_session)
):
    usuario = session.get(UsersDB, user_id)

    if usuario is None:
        return {"erro": "Usuário não encontrado"}

    session.delete(usuario)
    session.commit()

    return {"msg": "Usuário deletado"}        
    