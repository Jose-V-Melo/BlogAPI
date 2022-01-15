from sqlalchemy import Column, Integer, TIMESTAMP, VARCHAR, Unicode
from sqlalchemy_utils import EmailType, PhoneNumberType, URLType
from src.infra.sqlalchemy.config.database import Base

from datetime import datetime

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column(VARCHAR(100), nullable=False)
    senha = Column(VARCHAR(150), nullable=False)
    email = Column(EmailType, unique=True, nullable=False)
    telefone = Column(PhoneNumberType('BR', 14), nullable=False)
    funcao = Column(Integer, nullable=False, default=3)
    foto = Column(URLType)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = Column(TIMESTAMP)

    def __repr__(self):
        return "<Usuario(nome='%s')>" % (self.nome)