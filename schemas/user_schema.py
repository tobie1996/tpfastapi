from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    email: str
    password: str


class GetOneUser(BaseModel):
    id: int
    username: str
    email: str
    password: str


class DeleteOneUser(BaseModel):
    id: int


class UpdateUser(BaseModel):
    id: int
    username: str
    email: str
    password: str
