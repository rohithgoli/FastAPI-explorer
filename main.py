from fastapi import FastAPI

app = FastAPI()


@app.get('/')   # path operation decorator (path & operator)
def index():    # path operation function
    return {
        "data": {
            "greeting": "blog list"
        }
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