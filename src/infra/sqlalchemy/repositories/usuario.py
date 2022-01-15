from datetime import datetime
from sqlalchemy import update, delete
from sqlalchemy.orm import Session
import src.schemas.usuario as schemas
import src.infra.sqlalchemy.models.usuario as models

class RepositoryUsuario():
    def __init__(self, session: Session):
        self.session = session

    def create(self, usuario: schemas.Usuario, foto_url: str):
        db_usuario = models.Usuario(**usuario.dict(), foto=foto_url)
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario

    def read(self):
        usuarios = self.session.query(models.Usuario).all()
        return usuarios

    def update(self, id_usuario: int, usuario: schemas.Usuario, foto_url: str):
        stmt = (
            update(models.Usuario).where(models.Usuario.id == id_usuario).
            values(**usuario.dict(), foto=foto_url)
        )
        self.session.execute(stmt)
        self.session.commit()

    def delete(self, id_usuario: int):
        stmt = delete(models.Usuario).where(models.Usuario.id == id_usuario)
        self.session.execute(stmt)
        self.session.commit()
