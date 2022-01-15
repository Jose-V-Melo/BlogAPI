from sqlalchemy import Column, Integer, TIMESTAMP, VARCHAR, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from src.infra.sqlalchemy.config.database import Base

from datetime import datetime

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column(VARCHAR(100), nullable=False)
    vlr_unit = Column(DECIMAL(4,2), nullable=False)
    tamanho = Column(VARCHAR(45), nullable=False)
    descricao = Column(VARCHAR(1000), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = Column(TIMESTAMP)
    categoria_id = Column(Integer, ForeignKey('categorias.id', name='fk_categoria'), nullable=False)

    categoria = relationship('Categoria', back_populates='produtos')

    def __repr__(self):
        return "<Produto(nome='%s')>" % (self.nome)