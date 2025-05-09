from app.models.user_model import User
from app.models.content_model import Content
from app.models.credential_model import Credential
from app.constants.roles import Rol

users = [
    User(id=0, name="User 1", last_name="last name 1", age=50),
    User(id=1, name="User 2", last_name="last name 2", age=25),
    User(id=2, name="User 3", last_name="last name 3", age=15)
]

contents = [
    Content(id=0, title="Contenido En Revisión", duration=120, content_url="https://fake-url.com", role_required=Rol.ADMIN),
    Content(id=1, title="Contenido Exclusivo", duration=160, content_url="https://fake-url.com", role_required=Rol.PRO),
    Content(id=2, title="Contenido Público", duration=57, content_url="https://fake-url.com", role_required=Rol.BASIC)
]

credentials = [
    Credential(user_id=0, api_key="user0", role=Rol.ADMIN),
    Credential(user_id=1, api_key="user1", role=Rol.PRO),
    Credential(user_id=2, api_key="user2", role=Rol.BASIC)
]