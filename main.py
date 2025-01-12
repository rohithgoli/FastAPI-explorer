from fastapi import FastAPI
from typing import Optional

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