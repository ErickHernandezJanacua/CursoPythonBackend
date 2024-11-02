from fastapi import FastAPI
from pydantic import BaseModel
from super_db import usuarios, items

app = FastAPI()

@app.get("/")
def get_base():
    return {"Mensaje": "Mundo"}

@app.get("/tarea-1")
def get_tarea1():
    return {"respuesta": "Primer tarea realizada"}


@app.get("/usuario/{id}")
def get_usuario(id: int):
    usuario = usuarios.get(id)
    if not usuario:
        return "No se encontró el usuario"
    return usuario


@app.put("/usuario/favorito")
def put_favorito(nombre: str, ultima_fecha: str, id: int):
    usuario = usuarios.get(id)
    if not usuario:
        return "No se encontró el usuario"
    usuario['favoritos'].append({
        "nombre": nombre, "ultima-fecha": ultima_fecha})
    return usuario


@app.get("/item")
def get_usuario(id: str):
    item = items.get(id)
    if not item:
        return "No se encontró el item"
    return item


class Usuario(BaseModel):
    nombre: str
    apellido: str
    edad: int
    favoritos: list

@app.post("/usuario")
def post_usuario(usuario: Usuario):
    ultimo_id = len(usuarios)
    usuarios[ultimo_id + 1] = usuario.model_dump()
    print(usuarios)
    return "Guardado"
