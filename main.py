from fastapi import FastAPI

from database import engine
from models import Base

app = FastAPI()

# Create database tables on startup
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello, world. I built this."}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}, this app is alive on the internet."}

@app.get("/messages")
def create_message(text: str):
    db = SessionLocal()
    message = db.query(Message).all()
    db.close()
    return messages