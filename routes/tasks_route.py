

from fastapi import APIRouter, Depends, HTTPException
from crud.crud_task import create_Task, get_all_Task, get_task
from sqlalchemy.orm import Session
from database import get_db
from schemas.task_schemas import CreateTask, GetTask, UpdateTask


tasks_router = APIRouter(
    prefix='/tasks',
    tags=['tasks management']

)


# LAS GESTION DES TASKS


@tasks_router.post("/task/add_task")
def create_task(task: CreateTask, db: Session = Depends(get_db)):
    db_task = create_Task(db, task)
    return db_task


@tasks_router.delete("/delete_task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    delete_task(db, task_id)
    return {"message": "Utilisateur supprimé"}


@tasks_router.get("/get_task/{task_id}", response_model=GetTask)
def get_one_task(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return db_task


@tasks_router.get("/tasks/get_all_task")
def get_alls_tasks(db: Session = Depends(get_db)):
    tasks = get_all_Task(db)
    return tasks


@tasks_router.put("/task/update_task", response_model=UpdateTask)
def update_task(task: UpdateTask, db: Session = Depends(get_db)):
    db_task = update_task(db, task)
    return db_task


@tasks_router.get("/tasks/tasks/")
def filter_task(completed: str, db: Session = Depends(get_db)):
    tasks = filter_task(db, completed)
    return tasks
