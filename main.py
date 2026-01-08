from fastapi import FastAPI

from database import engine, SessionLocal
from models import Base, Message

app = FastAPI()

# Create database tables on startup
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello, world. I built this."}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}, this app is alive on the internet."}

@app.get("/messsages")
def read_messages():
    db = SessionLocal()
    messages = db.query(Message).all()
    db.close()
    return messages

@app.post("/messages")
def create_message(text: str):
    db = SessionLocal()
    message = Message(text=text)
    db.add(message)
    db.commit()
    db.refresh(message)
    db.close()
    return {"id": message.id, "text": message.text}