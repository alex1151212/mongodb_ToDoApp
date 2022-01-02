from pydantic import BaseModel

class Todo(BaseModel):
    title:str
    description:str

class Account(BaseModel):
    id:str
    password:str
    title:str