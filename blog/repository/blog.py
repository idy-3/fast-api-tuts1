from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(req: schemas.Blog, db: Session):
    new_blog = models.Blog(title=req.title,body=req.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update(id:int, req: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found")
    
    blog.update(req)
    return {"detail": "Updated"}


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail': 'done'}

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail' : f"Blog with the id {id} is not available"}

    return blog