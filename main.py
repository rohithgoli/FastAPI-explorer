from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/blog')   # path operation decorator (path & operator)
def index(limit=10, published: bool = True, sort: Optional[str] = None):    # path operation function
    if published:
        return {
            'data': f"{limit} published blogs from the db"
        }
    else:
        return {
            "data": f"{limit} blogs from the db"
        }


@app.get('/blog/unpublished')
def unpublished():
    return {
        'data': 'all unpublished blogs'
    }


@app.get('/blog/{id}')
def show_blog(id: int):
    #  fetch blog with id = id
    return {
        'data': id
    }


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {
        'data': ['1', '2']
    }


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    pass


@app.post('/blogs')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)