from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from ..repository import blog
from .. import schemas, database, oauth2

router = APIRouter(prefix="/blogs", tags=['Blogs'])

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2. get_current_user)):
   return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(req: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2. get_current_user)):
    return blog.create(req, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2. get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, req: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2. get_current_user)):
    return blog.update(id, req, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2. get_current_user)):
    return blog.show(id, db)