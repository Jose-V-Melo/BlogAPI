from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Produtos_Categoria(BaseModel):
    id: int
    nome: str
    valor: float

class Categoria(BaseModel):
    id: Optional[int]
    tipo: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    produtos: List[Produtos_Categoria]

    class Config:
        orm_mode = True