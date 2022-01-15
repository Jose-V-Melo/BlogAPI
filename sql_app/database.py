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
SQLALCHEMY_DATABASE_URL = "postgresql://yfvkusxjtlhuha:1d5b1a1b4791f1524544d94ceab5ded6ec8748fd1c58f199e41162ce8473db7e@ec2-54-196-105-177.compute-1.amazonaws.com:5432/dfoken5lgc89eo"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
