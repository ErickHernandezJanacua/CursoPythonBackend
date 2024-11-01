from fastapi import FastAPI
from super_db import usuarios, items

app = FastAPI()

@app.get("/")
def get_base():
    return {"Mensaje": "Mundo"}

# @app.get("/tarea-1")
# def get_tarea1():
#     return {"respuesta": "Primer tarea realizada"}


@app.get("/usuario/{id}")
def get_usuario(id: int):
    usuario = usuarios.get(id)
    print(usuario)
