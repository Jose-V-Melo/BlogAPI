from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import usuario, categoria, produto

app = FastAPI()

origins = [
    "https://192.168.100.18:4000",
    "https://pizzarialuigi.ddns.net",
    "http://localhost:4000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(usuario.router)
app.include_router(categoria.router)
app.include_router(produto.router)