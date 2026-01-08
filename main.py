from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from database import engine, SessionLocal
from models import Base, Message

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Create database tables on startup
Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}, this app is alive on the internet."}

@app.get("/messages")
def read_messages():
    db = SessionLocal()
    messages = db.query(Message).all()
    db.close()
    return [{"id": m.id, "text": m.text} for m in messages]

@app.post("/messages")
def create_message(text: str):
    db = SessionLocal()
    message = Message(text=text)
    db.add(message)
    db.commit()
    db.refresh(message)
    db.close()
    return {"id": message.id, "text": message.text}

