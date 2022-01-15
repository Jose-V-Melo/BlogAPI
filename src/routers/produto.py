from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.schemas.produto import Produto
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.produto import RepositoryProduto

router = APIRouter()

@router.post("/produtos", status_code=status.HTTP_201_CREATED, response_model=Produto)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositoryProduto(db).create(produto)
    return produto_criado

@router.get("/produtos", response_model=List[Produto])
def listar_produto(db: Session = Depends(get_db)):
    produtos = RepositoryProduto(db).list()
    return produtos