from fastapi import FastAPI,HTTPException, responses
from fastapi.middleware.cors import CORSMiddleware
from model import Todo,Account
import uvicorn

app = FastAPI()

from database_Todo import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

from database_Account import (
    fetch_one_account,
    fetch_all_accounts,
    create_account,
    update_account,
    remove_account,
)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=['*'],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Ping":"Pong"}



@app.get("/api/todo", tags=["Todo"])
async def get_todo():
    response = await fetch_all_todos()
    return response 

@app.get("/api/todo/{title}",response_model=Todo, tags=["Todo"])
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404,f"there is no TODO item with this {title}")

@app.post("/api/todo",response_model=Todo, tags=["Todo"])
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400,"Something went wrong / Bad Request")

@app.put("/api/todo/{title}",response_model=Todo, tags=["Todo"])
async def put_todo(title:str,desc:str):
    response = await update_todo(title,desc)
    if response:
        return response
    raise HTTPException(404,f"there is no TODO item with this {title}")


@app.delete("/api/todo/{title}", tags=["Todo"])
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Succesfully deleted todoo item !"
    raise HTTPException(404,f"there is no TODO item with this {title}")

# if __name__ == "__main__":
#     uvicorn.run("main:app",host='0.0.0.0',port=8000,reload=True,debug=True)


@app.get("/api/account", tags=["Account"])
async def get_account():
    response = await fetch_all_accounts()
    return response 

@app.get("/api/account/{title}",response_model=Account, tags=["Account"])
async def get_account_by_title(title):
    response = await fetch_one_account(title)
    if response:
        return response
    raise HTTPException(404,f"there is no Account item with this {title}")

@app.post("/api/account",response_model=Account, tags=["Account"])
async def post_account(account:Account):
    response = await create_account(account.dict())
    if response:
        return response
    raise HTTPException(400,"Something went wrong / Bad Request")

@app.put("/api/account/{title}",response_model=Account, tags=["Account"])
async def put_account(id:str,pw:str,title:str):
    response = await update_account(id,pw,title)
    if response:
        return response
    raise HTTPException(404,f"there is no Account item with this {title}")


@app.delete("/api/account/{id}", tags=["Account"])
async def delete_account(title):
    response = await remove_account(title)
    if response:
        return "Succesfully deleted todoo item !"
    raise HTTPException(404,f"there is no TODO item with this {title}")

