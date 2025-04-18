from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services import user_services
from app.models.user_model import User

router = APIRouter()

@router.get("")
def get_all_users():
    users = user_services.get_all_users()

    return JSONResponse(
        status_code=200,
        content={
            "success" : True,
            "data" : [user.model_dump() for user in users]
        }
    )

@router.get("/{user_id}")
def get_user(user_id: int):
    user = user_services.get_user(user_id)

    if user:
        return JSONResponse(
            status_code=200,
            content={
                "success" : True,
                "data" : user.model_dump()
            }
        )
    else:
        return JSONResponse(
            status_code=404,
            content={
                "success" : False,
                "status_code" : 404,
                "message" : f"El usuario {user_id} no existe!"
            }
        )
    
@router.post("")
def create_user(user: User):

    if user_services.create_user(user):
        return JSONResponse(
            status_code=201,
            content={
                "success" : True,
                "message" : f"Usuario {user.name} creado correctamente!"
            }
        )
    else:
        return JSONResponse(
            status_code=409,
            content={
                "success" : False,
                "message" : f"El id '{user.id}' ya está en uso!"
            }
        )
    
@router.put("")
def update_user(updated_user: User):
    if user_services.update_user(updated_user):
        return JSONResponse(
            status_code=200,
            content={
                "success" : True,
                "message" : f"El usuario '{updated_user.id}' ha sido actualizado correctamente!"
            }
        )
    else:
        return JSONResponse(
            status_code=404,
            content={
                "success" : False,
                "message" : f"El usuario '{updated_user.id}' no existe!"
            }
        )
    
@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_services.delete_user(user_id):
        return JSONResponse(
            status_code=200,
            content={
                "success" : True,
                "message" : f"El usuario '{user_id}' ha sido eliminado correctamente!"
            }
        )
    else:
        return JSONResponse(
            status_code=404,
            content={
                "success" : False,
                "message" : f"El usuario '{user_id} no existe!"
            }
        )