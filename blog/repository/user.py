from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .. import models, schemas
from ..hashing import Hash

def create(req: schemas.User, db: Session):
    req.password = Hash.bcrypt(req.password) 
    new_user = models.User(**req.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not found")

    return user