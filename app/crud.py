from sqlalchemy.orm import Session
from passlib.context import CryptContext

from . import models, schemas

password_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash_password(password: str):
    return password_context.hash(password)

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)

    db_user = models.User(first_name=user.first_name, last_name=user.last_name, email=user.email, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user