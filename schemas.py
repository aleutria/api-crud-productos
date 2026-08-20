from pydantic import BaseModel, Field, ConfigDict

class ProductoRespuesta(BaseModel):
    id: int
    nombre: str = Field(min_length=1)
    cantidad: int = Field(gt=0)
    model_config = ConfigDict(from_attributes=True)

class Producto(BaseModel):
    nombre: str = Field(min_length=1)
    cantidad: int = Field(gt=0)

class ProductoActualizar(BaseModel):
    cantidad: int = Field(gt=0)