from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from blog.database import get_db
from blog import schemas, models
from blog.hashing import Hash
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)