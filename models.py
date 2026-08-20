from database import Base
from sqlalchemy import Column, Integer, String

class ProductoDB(Base): # creamos el modelo base en forma de tabla en sqlalchemy con 3 columnas id, nombre, cantidad.
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String,nullable=False)
    cantidad = Column(Integer, nullable=False)