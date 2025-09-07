from fastapi import FastAPI, Form
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2004skate",
    database="mydb"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"messege":"Hello world"}

@app.get("/get_tasks")
def get_tasks():
    cursor=conn.cursor(dictionary=True)
    cursor.execute("select * from todo")
    records=cursor.fetchall()
    return records

@app.post("/add_tasks")
def add_tasks(task:str=Form(...)):
    cursor=conn.cursor()
    cursor.execute("insert into todo (task) values (%s)", (task,))
    conn.commit()
    return "Added Succesfully"

@app.post("/delete_tasks")
def add_tasks(id:str=Form(...)):
    cursor=conn.cursor()
    cursor.execute("delete from todo where id=%s", (id,))
    conn.commit()
    return "Deleted Succesfully"