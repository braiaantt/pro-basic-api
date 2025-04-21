from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from app.routes.user_routes import router as user_router
from app.routes.content_routes import router as content_router
from app.exceptions.handlers import  http_exception_handler, validation_exception_handler, general_exception_handler

app = FastAPI()

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

app.include_router(user_router, prefix="/users")
app.include_router(content_router, prefix="/contents")