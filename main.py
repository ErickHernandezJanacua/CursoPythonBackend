from fastapi import FastAPI

app = FastAPI

@app.get("/")
def get_base():
    return {"Mensaje": "Mundo"}

@app.get("/tarea-1")
def get_tarea1():
    return {"respuesta": "Primer tarea realizada"}

