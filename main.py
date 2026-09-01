from fastapi import FastAPI
from routers.productos import router as productos_router

app = FastAPI()

app.include_router(
    productos_router,
    prefix="/productos",
    tags=["productos"]
)

@app.get("/")
async def inicio():
    return "Mi primer backend"