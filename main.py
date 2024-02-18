from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from crud.crud_task import create_Task
from crud.crud_user import create_user
from models.model_task import Task
from schemas import task_schemas, user_schema
from schemas.task_schemas import CreateTask, UpdateTask
from models import model_task
from crud import crud_task, crud_user
from typing import List, Optional

from database import get_db
from schemas.user_schema import CreateUser

app = FastAPI()

# LAS GESTION DES TASKS


@app.post("/task/add_task")
def create_task(task: CreateTask, db: Session = Depends(get_db)):
    db_task = create_Task(db, task)
    return db_task


@app.delete("/delete_task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    crud_task.delete_task(db, task_id)
    return {"message": "Utilisateur supprimé"}


@app.get("/get_task/{task_id}", response_model=task_schemas.GetTask)
def get_one_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud_task.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return db_task


@app.get("/tasks/get_all_task")
def get_alls_tasks(db: Session = Depends(get_db)):
    tasks = crud_task.get_all_Task(db)
    return tasks


@app.put("/task/update_task", response_model=task_schemas.UpdateTask)
def update_task(task: task_schemas.UpdateTask, db: Session = Depends(get_db)):
    db_task = crud_task.update_task(db, task)
    return db_task


@app.get("/tasks/tasks/")
def filter_task(completed: str, db: Session = Depends(get_db)):
    tasks = crud_task.filter_task(db, completed)
    return tasks


# LAS GESTION DES USERS

@app.post("/users/add_user")
def create_users(user: CreateUser, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user


@app.delete("/delete_user/{user_id}")
def delete_users(user: int, db: Session = Depends(get_db)):
    crud_user.delete_user(db, user)
    return {"message": "Utilisateur supprimé"}


@app.get("/get_user/{user_id}", response_model=user_schema.GetOneUser)
def get_one_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_one_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return db_user


@app.get("/users/get_all_users")
def get_alls_users(db: Session = Depends(get_db)):
    users = crud_user.get_all_users(db)
    return users


@app.put("/users/update_users", response_model=user_schema.UpdateUser)
def update_user(user: user_schema.UpdateUser, db: Session = Depends(get_db)):
    db_user = crud_user.update_user(db, user)
    return db_user
