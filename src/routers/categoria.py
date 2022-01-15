from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.schemas.categoria import Categoria
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.categoria import RepositoryCategoria

router = APIRouter()

@router.post("/categorias", status_code=status.HTTP_201_CREATED, response_model=Categoria)
def criar_categoria(categoria: Categoria, db: Session = Depends(get_db)):
    categoria_criada = RepositoryCategoria(db).create(categoria)
    return categoria_criada

@router.get("/categorias", response_model=List[Categoria])
def listar_categorias(db: Session = Depends(get_db)):
    categorias = RepositoryCategoria(db).list()
    return categorias