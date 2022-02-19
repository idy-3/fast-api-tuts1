from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import database, schemas
from ..repository import user 

get_db = database.get_db

router = APIRouter(tags=["Users"], prefix="/user")

@router.post('/', response_model=schemas.ShowUser)
def create_user(req: schemas.User, db: Session = Depends(get_db)):
    return user.create(req, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.get_user(id, db)