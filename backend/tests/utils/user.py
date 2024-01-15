from sqlalchemy.orm import Session
from backend.db.repository.user import create_new_user
from backend.schemas.user import UserCreate


def create_random_user(db: Session):
    user = UserCreate(email="test@gmail.com", password="password")
    user = create_new_user(user=user, db=db)
    return user


