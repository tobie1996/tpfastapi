from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from crud.crud_user import create_user, delete_user, get_all_users
from database import get_db
from schemas.user_schema import CreateUser, GetOneUser, UpdateUser


users_router = APIRouter(
    prefix='/users',
    tags=['users management']

)


# LAS GESTION DES USERS

@users_router.post("/users/add_user")
def create_users(user: CreateUser, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user


@users_router.delete("/delete_user/{user_id}")
def delete_users(user: int, db: Session = Depends(get_db)):
    delete_user(db, user)
    return {"message": "Utilisateur supprimé"}


@users_router.get("/get_user/{user_id}", response_model=GetOneUser)
def get_one_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_one_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return db_user


@users_router.get("/users/get_all_users")
def get_alls_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users


@users_router.put("/users/update_users", response_model=UpdateUser)
def update_user(user: UpdateUser, db: Session = Depends(get_db)):
    db_user = update_user(db, user)
    return db_user
