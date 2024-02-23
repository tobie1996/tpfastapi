import inspect
import re
from fastapi import APIRouter, FastAPI
from sqlalchemy.orm import Session
from models.model_task import Task
from crud import crud_task, crud_user
from typing import List, Optional
from fastapi_jwt_auth import AuthJWT
from fastapi.routing import APIRoute
from routes.users_route import users_router
from routes.tasks_route import tasks_router

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
