from typing import List
from fastapi import APIRouter, status, Depends, UploadFile, File
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.usuario import Usuario, UsuarioSimples
from src.infra.sqlalchemy.repositories.usuario import RepositoryUsuario

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UsuarioSimples)
def signup(usuario: Usuario, image_file: UploadFile = File(...), db: Session = Depends(get_db)):
    usuario_criado = RepositoryUsuario(db).create(usuario)
    return usuario_criado

@router.get("/usuarios", response_model=List[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositoryUsuario(db).read()
    return usuarios

@router.put("/usuario/{id_usuario}")
def editar_usuario(id_usuario, usuario: Usuario, db: Session = Depends(get_db)):
    RepositoryUsuario(db).update(id_usuario, usuario)
    return usuario

@router.delete("/usuario/{id_usuario}")
def excluir_usuario(id_usuario, db: Session = Depends(get_db)):
    RepositoryUsuario(db).delete(id_usuario)
    return {"mensagem": "Usuário excluído com sucesso!"}