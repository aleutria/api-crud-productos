from database import conectar_db_sqlalchemy
from models import ProductoDB
from sqlalchemy import select

def insertar_producto_sqlalchemy(nombre, cantidad):
    db = conectar_db_sqlalchemy()
    producto = ProductoDB(
        nombre=nombre,
        cantidad=cantidad
    )
    db.add(producto)
    db.commit()
    db.close()

def obtener_productos_sqlalchemy():
    db = conectar_db_sqlalchemy()
    consulta = select(ProductoDB)  # selecciono PorductoDb como el sitio donde realizar la consulta
    resultado = db.execute(consulta)
    productos = resultado.scalars().all() # scalars()- obtener los objetos q vienen de la consutla en vez de trabajar con filas/tuplas,dame los objetos, valores principales del resultado
    db.close()
    return productos

def buscar_producto_sqlalchemy(nombre):
    db = conectar_db_sqlalchemy()
    consulta = select(ProductoDB).where(ProductoDB.nombre==nombre) # busca el producto cuyo nombre sea igual al q escribí
    resultado = db.execute(consulta) # aqui ejecuta la consulta utilizando la sesion
    producto = resultado.scalar_one_or_none() # scalar_one_or_none() → devuelve uno o ninguno.
    db.close()
    return producto

def actualizar_producto_sqlalchemy(nombre, cantidad):
    db = conectar_db_sqlalchemy()
    consulta = select(ProductoDB).where(ProductoDB.nombre==nombre)
    resultado = db.execute(consulta)
    producto = resultado.scalar_one_or_none()
    if producto is not None:
        producto.cantidad = cantidad
    db.commit()
    db.close()
    return producto

def eliminar_producto_sqlalchemy(nombre):
    db = conectar_db_sqlalchemy()
    consulta = select(ProductoDB).where(ProductoDB.nombre==nombre)
    resultado = db.execute(consulta)
    producto = resultado.scalar_one_or_none()
    if producto is not None:
        db.delete(producto)
        db.commit()
    db.close()
    return producto