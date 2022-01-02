from model import Account, Todo

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://127.0.0.1:27017/')
database = client.AccountList
collection = database.account

async def fetch_one_account(title):
    document = await collection.find_one({"title":title})
    return document

async def fetch_all_accounts():
    accounts=[]
    cursor = collection.find({})
    async for document in cursor:
        accounts.append(Account(**document))
    return accounts

async def create_account(account):
    document = account
    result = await collection.insert_one(document)
    return document

async def update_account(id,pw,title):
    await collection.update_one({"title":title},{"$set":{
        "id":id,
        "password":pw,
    }})
    
    document = await collection.find_one({"title":title})
    return document

async def remove_account(id):
    await collection.delete_one({"id":id})
    return True

#-----------------------------------------------------


    