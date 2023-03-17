from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
# from typing import Optional, List
# from sqlalchemy import Column, String, Integer,Date

from models import models


from config.db import BASE,engine, sessionlocal

from sqlalchemy.orm import Session

class Todo(BaseModel):

    name: str
    due_date: str
    description: str



app = FastAPI(title="Todo API")

BASE.metadata.create_all(bind = engine)


def get_db():

    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()


# Create, Read, Update, Delete

store_todo = []

@app.get('/')
async def home(db : Session = Depends(get_db)):
    # return {"Hello": "World"}
    return db.query(models.TODO).all()

@app.post('/todo/')
async def create_todo(todo: Todo,db : Session = Depends(get_db)):
    # store_todo.append(todo)

    todo_model = models.TODO()

    todo_model.name = todo.name
    todo_model.description = todo.description


    db.add(todo_model)
    db.commit()



    return todo

# @app.get('/todo/', response_model=List[Todo])
# async def get_all_todos():
#     return store_todo

@app.get('/todo/{id}')
async def get_todo(id: int,db : Session = Depends(get_db) ):

    todo_model = db.query(models.TODO).filter(models.TODO.id == id).first()

    if todo_model is None:

        raise HTTPException(status_code=404, detail="Todo Not Found")
    
    else:

        return todo_model



@app.put('/todo/{id}')
async def update_todo(id: int, todo: Todo,db : Session = Depends(get_db) ):

    

    todo_model = db.query(models.TODO).filter(models.TODO.id == id).first()

    if todo_model is None:

        raise HTTPException(status_code=404, detail="Todo Not Found")
    
    else:

        todo_model.name = todo.name
        todo_model.description = todo.description
        db.add(todo_model)
        db.commit()

    return todo


@app.delete('/todo/{id}')
async def delete_todo(id: int,db : Session = Depends(get_db)):


    todo_model = db.query(models.TODO).filter(models.TODO.id == id)

    if(todo_model is None):
        raise HTTPException(status_code=404, detail="Todo Not Found")

    else:
        db.query(models.TODO).filter(models.TODO.id == id).delete()

        db.commit()




    