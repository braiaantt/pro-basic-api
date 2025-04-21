from pydantic import BaseModel
from app.constants.roles import Rol

class Credential(BaseModel):
    user_id: int
    api_key: str
    role: Rol