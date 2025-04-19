from app.models.user_model import User
from app.models.content_model import Content
from app.constants.roles import Rol

users = [
    User(id=0, name="User 1", last_name="last name 1", age=50, rol=Rol.ADMIN, api_key="user0"),
    User(id=1, name="User 2", last_name="last name 2", age=25, rol=Rol.PRO, api_key="user1"),
    User(id=2, name="User 3", last_name="last name 3", age=15, rol=Rol.BASIC, api_key="user2")
]

contents = [
    Content(id=0, title="Contenido En Revisión", duration=120, content_url="url", rol_requiered=Rol.ADMIN),
    Content(id=1, title="Contenido Exclusivo", duration=160, content_url="url", rol_requiered=Rol.PRO),
    Content(id=2, title="Contenido Público", duration=57, content_url="url", rol_requiered=Rol.BASIC)
]