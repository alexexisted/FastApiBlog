from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db.session import get_db
from backend.schemas.blog import ShowBlog, CreateBlog, UpdateBlog
from backend.db.repository.blog import create_new_blog, retreive_blog, list_blogs, update_blog

from typing import List

router = APIRouter()


@router.post("/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog


@router.get("/blog/{id}", response_model=ShowBlog)
async def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(detail=f"Blog with id {id} does not exist")
    return blog


@router.get("/blogs", response_model=List[ShowBlog])
async def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs


@router.put("/blog/{id}", response_model=ShowBlog)
def update_a_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db)):
    blog = update_blog(id=id, blog=blog, db=db, author_id=1)
    if not blog:
        raise HTTPException(detail=f"Blog with this id: {id} does not exist")
    return blog



