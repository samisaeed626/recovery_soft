from fastapi import FastAPI
from pydantic import BaseModel




app=FastAPI()

class users(BaseModel):
   
    id=int
    username=str
    fullname=str
    is_franchiser=bool
    is_deler=bool
    area=str
    password:str





@app.get('/',status_code=200)
def getcar_info():
    return{"message":"server is running"}


@app.get('/getpersonbyid/{person_id}',status_code=200)
def getpersonbyid(person_id:int):
    return {
        "message":person_id
    }


@app.post('/addperson',status_code=200)
def addperson_info(person:person):
    return{
        "id":person.id,
"firstname":person.firstname,
"lastname":person.lastname,
"male":person.ismale



    }
