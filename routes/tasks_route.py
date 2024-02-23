

from fastapi import APIRouter, Depends, HTTPException
from crud.crud_task import create_Task, delete_task, filter_task, get_all_Task, get_task, update_task
from sqlalchemy.orm import Session
from database import get_db
from schemas.task_schemas import CreateTask, UpdateTask


tasks_router = APIRouter(
    prefix='/tasks',
    tags=['tasks management']

)


# LAS GESTION DES TASKS


@tasks_router.post("/add")
def create_task(task: CreateTask, db: Session = Depends(get_db)):
    db_task = create_Task(db, task)
    return db_task


@tasks_router.delete("/delete/{task_id}")
def delete_tasks(task_id: int, db: Session = Depends(get_db)):
    delete_task(db, task_id)
    return {"message": "tache supprimée"}


@tasks_router.get("/get/{task_id}")
def get_one_tasks(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="tache non trouvé")
    return db_task


@tasks_router.get("/get_all")
def get_alls_tasks(db: Session = Depends(get_db)):
    tasks = get_all_Task(db)
    return tasks


@tasks_router.put("/update")
def update_tasks(task: UpdateTask, db: Session = Depends(get_db)):
    db_task = update_task(db, task)
    return db_task


@tasks_router.get("/filter")
def filter_tasks(completed: str, db: Session = Depends(get_db)):
    tasks = filter_task(db, completed)
    return tasks
