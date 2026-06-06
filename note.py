from fastapi import APIRouter, Depends, HTTPException 
from sqlmodel import Session

from depedencies import get_session
from models import NotesDB
from schemas import NoteCreate

router = APIRouter()

@router.post("/user/{user_id}/notes")
def criar_notas(user_id: int, note: NoteCreate, session: Session = Depends(get_session)):
    usuario = session.get(UsersDB, user_id)
    if usuario is None:
        raise HTTPException(
            status_code=400,
            deatil= "usuário não existe"
        )
    nova_nota= NotesDB(title = note.title, conteudo=note.conteudo, owner_id= user_id)
    
    session.add(nova_nota)
    session.commit()
    session.refresh(nova_nota)
    
    return nova_nota
    