from fastapi import HTTPException, Depends
from app.constants.roles import Rol
from app.middlewares.auth import authenticate_user
from app.services import credential_services
from app.services import content_services

def admin_rol(user = Depends(authenticate_user)):

    user_rol = credential_services.get_user_rol(user.id)

    if user_rol < Rol.ADMIN:
        raise HTTPException(status_code=403, detail="Acceso restringido")
    
    #if you want you can return user

def rol_required(content_id:int, user = Depends(authenticate_user)):

    user_rol = credential_services.get_user_rol(user.id)
    content = content_services.get_content(content_id)

    if not content:
        raise HTTPException(status_code=404, detail="El contenido solicitado no existe!")

    if user_rol < content.role_required:
        raise HTTPException(status_code=403, detail="Acceso restringido")

    return content
