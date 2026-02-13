from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()
# Cors: Mecanismo de seguridad. Se utiliza para habilitar peticiones desde clientes que no estan en mi dominio.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
@app.get("/sumar")
def sumar_numeros(a:float, b:float):
    return a+b

