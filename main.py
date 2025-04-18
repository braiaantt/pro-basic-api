from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def init():
    return {"message" : "Hola mundo!"}