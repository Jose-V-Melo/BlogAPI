from sqlalchemy.orm import Session
import src.schemas.produto as schemas
import src.infra.sqlalchemy.models.produto as models

class RepositoryProduto():
    def __init__(self, session: Session):
        self.session = session

    def create(self, produto: schemas.Produto):
        db_produto = models.Produto(**produto.dict())
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def list(self):
        produtos = self.session.query(models.Produto).all()
        return produtos

    def get(self):
        pass

    def delete(self):
        pass