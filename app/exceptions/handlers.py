from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success" : False,
            "message" : exc.detail,
            "code" : exc.status_code
        }
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "success" : False,
            "message" : "Valor ingresado no válido!",
            "errors" : exc.errors(),
            "code" : 422
        }
    )

async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success" : False,
            "message" : "Ocurrió un error inesperado",
            "code" : 500
        }
    )