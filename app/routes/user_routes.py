from fastapi import APIRouter, HTTPException, Depends
from app.services import user_services
from app.models.user_model import User
from app.middlewares import auth, verifiy

router = APIRouter()

@router.get("/", status_code=200, dependencies=[Depends(verifiy.admin_rol)])
def get_all_users():
    users = user_services.get_all_users()

    if len(users) != 0:
        return {"success" : True,
                "data" : [user.model_dump() for user in users]}
    
    else:
        raise HTTPException(status_code=404, detail="La lista de usuarios está vacía!")


@router.get("/me")
def get_my_user(user = Depends(auth.authenticate_user)):
    return {"success" : True,
            "data" : user.model_dump()}


@router.get("/{user_id}", status_code=200, dependencies=[Depends(verifiy.admin_rol)])
def get_user(user_id: int):
    user = user_services.get_user(user_id)

    if user:
        return {"success" : True,
                "data" : user.model_dump()}
    else:
        raise HTTPException(status_code=404, detail=f"El usuario {user_id} no existe!")


@router.post("/", status_code=201)
def create_user(user: User):

    if user_services.create_user(user):
        return {"success" : True,
                "message" : f"Usuario {user.name} creado correctamente!"}
    else:
        raise HTTPException(status_code=409, detail=f"El id {user.id} ya está en uso!")
        
    
@router.put("/me", status_code=200,)
def update_user(updated_user: User, user = Depends(auth.authenticate_user)):
    
    if updated_user.id != user.id:
        raise HTTPException(status_code=403, detail="No tienes permiso de modificar este usuario!")

    if user_services.update_user(updated_user):
        return {"success" : True,
                "message" : f"El usuario '{updated_user.id}' ha sido actualizado correctamente!"}
    else:
        raise HTTPException(status_code=404, detail=f"El usuario {updated_user.id} no existe!")


@router.delete("/me", status_code=200)
def delete_user(user = Depends(auth.authenticate_user)):
    if user_services.delete_user(user.id):
        return {"success" : True,
                "message" : f"El usuario '{user.id}' ha sido eliminado correctamente!"}
    else:
        raise HTTPException(status_code=404, detail=f"El usuario {user.id} no existe!")