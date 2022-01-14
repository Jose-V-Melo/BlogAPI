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
SQLALCHEMY_DATABASE_URL = "postgresql://nkqwpdjewpdzkc:f4281a5231877ecf0c998dcc8844a16bab33308e32d0d2da58096ca7c833bd35@ec2-3-232-22-121.compute-1.amazonaws.com:5432/dp8aibl5jnn6c"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
