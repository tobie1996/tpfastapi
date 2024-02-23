import inspect
import re
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from crud.crud_task import create_Task
from crud.crud_user import create_user
from models.model_task import Task
from schemas import task_schemas, user_schema
from schemas.task_schemas import CreateTask, UpdateTask
from models import model_task
from crud import crud_task, crud_user
from typing import List, Optional
from fastapi_jwt_auth import AuthJWT
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute
from routes.users_route import users_router
from routes.tasks_route import tasks_router


from database import get_db

app = FastAPI(
    title="TACHES UTILISATEURS",
    version="0.1.0",
    openapi_url="/openapi.json",
    description="Cette application permet au super utilisateurs de donner des autorisations aux utilisateurs",

)


# GESTION DES TASK

app.include_router(tasks_router)

# GESTION DES UTILISATEURS


app.include_router(users_router)
