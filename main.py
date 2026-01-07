from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Item

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/items")
def list_items(db: Session = Depends(get_db)):
    return db.query(Item).all()