from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Categoria_Produto(BaseModel):
    tipo: str

class Produto(BaseModel):
    id: Optional[int]
    nome: str
    valor: float
    tamanho: str
    descricao: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    categoria_id: int
    categoria: Optional[Categoria_Produto]

    class Config:
        orm_mode = True