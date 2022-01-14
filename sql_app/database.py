from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import cloudinary

cloudinary.config(
    cloud_name="pizzarialuigi-ddns-net",
    api_key="212123817192666",
    api_secret="h90KfxTzbvbIusX16Uk9XsojKpQ"
)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgres://bgtjzctiuiojfz:34c05328ccbcbce69cca0ba20c4ce4d1b148d1cdb1e49188d29888b222019b30@ec2-54-87-92-21.compute-1.amazonaws.com:5432/ddhnrrjkfl7m03"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
