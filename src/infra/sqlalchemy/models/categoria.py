from sqlalchemy import Column, Integer, TIMESTAMP, VARCHAR
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

from datetime import datetime

class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tipo = Column(VARCHAR(45), nullable=False, unique=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = Column(TIMESTAMP)

    produtos = relationship('Produto', back_populates='categoria')

    def __repr__(self):
        return '<Categoria %r>' % self.tipo