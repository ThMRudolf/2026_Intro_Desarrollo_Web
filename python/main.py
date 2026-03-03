from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/info")
def read_info():
    return {"nombre": "Thomas", "edad": "48", "color favorito": "#057029"}    