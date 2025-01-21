from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"message": "Hey there, how are you doing"}
