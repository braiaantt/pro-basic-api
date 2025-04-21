from fastapi import HTTPException, Depends
from app.constants.roles import Rol
from app.middlewares.auth import authenticate_user
from app.services import credential_services

def admin_rol(user = Depends(authenticate_user)):

    user_rol = credential_services.get_user_rol(user.id)

    if user_rol < Rol.ADMIN:
        raise HTTPException(status_code=403, detail="Acceso restringido")
    
    #if you want you can return user

    


