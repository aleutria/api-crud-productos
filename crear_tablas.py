from database import Base, engine
from models import ProductoDB

Base.metadata.create_all(engine)