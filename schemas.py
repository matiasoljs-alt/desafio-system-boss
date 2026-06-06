from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    
class NoteCreate(BaseModel):
    title: str
    conteudo: str
    
    