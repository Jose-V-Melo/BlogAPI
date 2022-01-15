from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Usuario(BaseModel):
    id: Optional[int]
    nome: str
    senha: str
    email: str
    telefone: str
    funcao: Optional[int]
    foto: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str

    class Config:
        orm_mode = True