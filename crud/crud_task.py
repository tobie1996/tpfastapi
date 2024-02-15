from sqlalchemy.orm import Session
from models.model_task import Task
from schemas import task_schemas
from schemas.task_schemas import CreateTask, UpdateTask
from models import model_task
from typing import List, Optional

# pour creer une tache


def create_Task(db: Session, task: CreateTask):
    db_create = Task(
        task=task.task,
        completed=task.completed
    )
    db.add(db_create)
    db.commit()
    db.refresh(db_create)
    return db_create

# pour suprimer une tache


def delete_task(db: Session, task_id: int):
    db.query(model_task.Task).filter(model_task.Task.id == task_id).delete()
    db.commit()


# Afficher une seule tache:


def get_task(db: Session, task_id: int):
    return db.query(model_task.Task).filter(model_task.Task.id == task_id).first()


# pour afficher toutes les tach


def get_all_Task(db: Session):
    return db.query(model_task.Task).all()


# pour afficher toutes les taches


def update_task(db: Session, task: task_schemas.UpdateTask):
    db_task = db.query(model_task.Task).filter(
        model_task.Task.id == task.id).first()
    db_task.task = task.task,
    db_task.completed = task.completed,

    db.commit()
    db.refresh(db_task)
    return db_task

# operation des filtrage


def get_tasks(db: Session, completed: Optional[bool]):
    if completed is not None:
        tasks = db.query(Task).filter(Task.completed == completed).all()
    else:
        tasks = db.query(Task).all()  # Return all tasks if completed is None

    return tasks
