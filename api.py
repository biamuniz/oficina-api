from fastapi import FastAPI, HTTPException, Depends
import services, schemas, models
from database import engine, get_db
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/") ### método http de leitura
def read_hello_world():
    return {"message": "Hello World"}

## inserir usuário no banco

@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db=db, user=user)