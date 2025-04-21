from fastapi import Request, HTTPException
from app.services import credential_services

def authenticate_user(request: Request):
    api_key = request.headers.get("authorization")

    if not api_key:
        raise HTTPException(status_code=401, detail="Sin header de autorizacion!") 

    user = credential_services.get_user(api_key)

    if  user:
       return user
    else:
        raise HTTPException(status_code=401, detail="Usuario no registrado!")