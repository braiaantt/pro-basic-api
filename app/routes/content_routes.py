from fastapi import APIRouter, HTTPException, Depends
from app.models.content_model import Content
from app.services import content_services
from app.middlewares import auth, verifiy

router = APIRouter()

@router.get("/", status_code=200, dependencies=[Depends(auth.authenticate_user)])
def get_public_contents():
    contents = content_services.get_public_contents()

    if len(contents) > 0:

        return {"success" : True,
                "data" : [content.model_dump() for content in contents]}
    
    raise HTTPException(status_code=404, detail="La lista de contenido está vacía")

@router.get("/{content_id}", status_code=200)
def get_content(content: Content = Depends(verifiy.rol_required)):

    return {"success" : True,
            "data" : content.model_dump()}

@router.post("/", status_code=201, dependencies=[Depends(verifiy.admin_rol)])
def add_content(content: Content):
    if not content.title or content.duration <= 0:
        raise HTTPException(status_code=400, detail="Datos del contenido invalidos")

    if content_services.add_content(content):
        return {"success" : True,
                "message" : "Contenido añadido correctamente!"}
    
    raise HTTPException(status_code=409, detail=f"El id '{content.id}' ya está en uso")

@router.put("/", status_code=200, dependencies=[Depends(verifiy.admin_rol)])
def update_content(content: Content):
    if content_services.update_content(content):
        return {"success" : True,
                "message" : "El contenido fue actualizado correctamente!"}

    raise HTTPException(status_code=404, detail="El contenido no existe!")

@router.delete("/{content_id}", status_code=200, dependencies=[Depends(verifiy.admin_rol)])
def delete_content(content_id: int):
    if content_services.delete_content(content_id):
        return {"success" : True,
                "message" : f"El contenido '{content_id}' fue eliminado correctamente"}