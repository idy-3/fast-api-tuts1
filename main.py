from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data': { 'name' : 'Heyy'} }

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id }

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1','2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):

    return {'data':f"Blog is created with {request.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
