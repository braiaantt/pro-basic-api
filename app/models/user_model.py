from pydantic import BaseModel
from app.constants.roles import Rol

class User(BaseModel):
    id: int
    name: str
    last_name: str
    age: int
    rol: Rol
    api_key: str