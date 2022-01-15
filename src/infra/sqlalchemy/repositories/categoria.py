from urllib.parse import scheme_chars
from sqlalchemy.orm import Session
import src.schemas.categoria as schemas
import src.infra.sqlalchemy.models.categoria as models

class RepositoryCategoria():
    def __init__(self, session: Session):
        self.session = session

    def create(self, categoria: schemas.Categoria):
        db_categoria = models.Categoria(**categoria.dict())
        self.session.add(db_categoria)
        self.session.commit()
        self.session.refresh(db_categoria)
        return db_categoria

    def list(self):
        categorias = self.session.query(models.Categoria).all()
        return categorias

    def get(self):
        pass

    def delete(self):
        pass