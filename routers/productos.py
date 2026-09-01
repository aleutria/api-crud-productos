from fastapi import APIRouter, HTTPException

from schemas import Producto, ProductoRespuesta, ProductoActualizar

from crud import (
    buscar_producto_sqlalchemy,
    obtener_productos_sqlalchemy,
    insertar_producto_sqlalchemy,
    actualizar_producto_sqlalchemy,
    eliminar_producto_sqlalchemy
)

router = APIRouter()


@router.get("/", response_model=list[ProductoRespuesta])
async def lista_productos():
    resultado = obtener_productos_sqlalchemy()
    return resultado

@router.get("/{nombre}", response_model=ProductoRespuesta)
async def obtener_producto(nombre):
    producto = buscar_producto_sqlalchemy(nombre)

    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return producto

@router.post("/", status_code=201)
async def crear_producto(producto: Producto):
    producto_existente = buscar_producto_sqlalchemy(producto.nombre)

    if producto_existente is not None:
        raise HTTPException(status_code=400, detail="El producto ya existe")
    insertar_producto_sqlalchemy(producto.nombre, producto.cantidad)

    return producto

@router.put("/{nombre}")
async def actualizar_producto(nombre, producto: ProductoActualizar):
    producto_existente = buscar_producto_sqlalchemy(nombre)

    if producto_existente is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    producto_actualizado = actualizar_producto_sqlalchemy(nombre, producto.cantidad)

    return producto_actualizado

@router.delete("/{nombre}", status_code=204)
async def eliminar_producto(nombre):
    producto_existente = buscar_producto_sqlalchemy(nombre)

    if producto_existente is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    eliminar_producto_sqlalchemy(nombre)