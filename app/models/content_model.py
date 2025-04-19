from pydantic import BaseModel
from app.constants.roles import Rol

class Content(BaseModel):
    id: int
    title: str
    duration: int
    content_url: str
    rol_requiered: Rol