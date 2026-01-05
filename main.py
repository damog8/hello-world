from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world. I built this."}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}, this app is alive on the internet."}