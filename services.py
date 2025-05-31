from http.client import HTTPException
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserUpdate



def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user