from fastapi import FastAPI, HTTPException
from schemas import Producto, ProductoActualizar, ProductoRespuesta
from crud import insertar_producto_sqlalchemy, obtener_productos_sqlalchemy, buscar_producto_sqlalchemy, actualizar_producto_sqlalchemy, eliminar_producto_sqlalchemy

app = FastAPI()

@app.get("/")
async def inicio():
    return "Mi primer backend"

@app.get("/productos", response_model=list[ProductoRespuesta])
async def lista_productos():
    resultado = obtener_productos_sqlalchemy()
    return resultado

@app.get("/productos/{nombre}", response_model=ProductoRespuesta)
async def obtener_producto(nombre):
    producto = buscar_producto_sqlalchemy(nombre)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.post("/productos", status_code=201)
async def crear_producto(producto: Producto):
    producto_existente = buscar_producto_sqlalchemy(producto.nombre)
    if producto_existente is not None:
        raise HTTPException(status_code=400, detail="El producto ya existe")
    insertar_producto_sqlalchemy(producto.nombre, producto.cantidad)
    return producto

@app.put("/productos/{nombre}")
async def actualizar_producto(nombre, producto: ProductoActualizar):
    producto_existente = buscar_producto_sqlalchemy(nombre)
    if producto_existente is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    producto_actualizado = actualizar_producto_sqlalchemy(nombre, producto.cantidad)
    return producto_actualizado

@app.delete("/productos/{nombre}", status_code=204)
async def eliminar_producto(nombre):
    producto_existente = buscar_producto_sqlalchemy(nombre)
    if producto_existente is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    eliminar_producto_sqlalchemy(nombre)


