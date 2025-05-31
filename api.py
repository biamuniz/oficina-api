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

#@app.post("/users")
#def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#    return services.create_user(db=db, user=user)

@app.get("/users/{user_email}")
def read_user_by_email(user_email: str, db:Session=Depends(get_db)):
    user = services.get_user_by_email(db=db, email=user_email)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = services.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    return services.create_user(db=db, user=user)