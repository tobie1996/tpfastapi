from sqlalchemy.orm import Session
from models.model_user import User
from schemas.user_schema import CreateUser
from models import model_user
from schemas import user_schema

# ajouter


def create_user(db: Session, user: CreateUser):
    db_create = User(username=user.username,
                     email=user.email, password=user.password)
    db.add(db_create)
    db.commit()
    db.refresh(db_create)
    return db_create

# recuperer tous les ussers


def get_all_users(db: Session):
    return db.query(model_user.User).all()

# recuperer un users uniquement


def get_one_user(db: Session, user_id: int):
    return db.query(model_user.User).filter(model_user.User.id == user_id).first()

# supprimer un user


def delete_user(db: Session, user_id: int):
    db.query(model_user.User).filter(model_user.User.id == user_id).delete()
    db.commit()

# modifier un users


def update_user(db: Session, user: user_schema.UpdateUser):
    db_user = db.query(model_user.User).filter(
        model_user.User.id == user.id).first()

    db_user.username = user.username,
    db_user.email = user.email,
    db_user.password = user.password,

    db.commit()
    db.refresh(db_user)
    return db_user
