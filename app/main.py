from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/users")
def read_users():
    # Implementation to read users from the JSON file
    ...

@app.post("/users")
def create_user():
    # Implementation to create a new user and store it in the JSON file
    ...
