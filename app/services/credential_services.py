from app.database.fake_database import credentials
from app.models.credential_model import Credential
from app.services import user_services
from app.constants.roles import Rol

def get_user(api_key: str):
    for credential in credentials:
        if credential.api_key == api_key:
            return user_services.get_user(credential.user_id)
    return None    

def get_user_rol(user_id: int):
    for credential in credentials:
        if credential.user_id == user_id:
            return credential.role
    return None

def set_user_credentials(user_id: int):
    api_key = f"user{user_id}"
    rol = Rol.BASIC
    new_credential = Credential(user_id=user_id, api_key=api_key, role=rol)
    credentials.append(new_credential)


def delete_credentials(user_id: int):
    for index, credential in enumerate(credentials):
        if credential.user_id == user_id:
            del credentials[index]
            return