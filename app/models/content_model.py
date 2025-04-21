from pydantic import BaseModel
from app.constants.roles import Rol

class Content(BaseModel):
    id: int
    title: str
    duration: int
    content_url: str
    role_required: Rol

class ContentPublic(BaseModel):
    id: int
    title: str
    role_required: Rol
