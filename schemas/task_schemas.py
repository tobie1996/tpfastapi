from pydantic import BaseModel


class CreateTask(BaseModel):
    task: str
    completed: str


class GetTask(BaseModel):
    task: str
    completed: str


class DeleteTask(BaseModel):
    id: int


class AllTasks(BaseModel):
    task: str
    completed: str


class GetOneTask(BaseModel):
    id: int


class UpdateTask(BaseModel):
    id: int
    task: str
    completed: str


class TaskBase(BaseModel):
    task: str


class Task(TaskBase):
    id: int
    completed: str
