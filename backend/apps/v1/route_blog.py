from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from typing import Optional
from sqlalchemy.orm import Session
from backend.db.session import get_db
from backend.db.repository.blog import list_blogs, retrieve_blog


templates = Jinja2Templates(directory="backend/templates")
router = APIRouter()


@router.get("/")
def home(request: Request, alert: Optional[str] = None, db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return templates.TemplateResponse("blog/home.html", {"request": request, "blogs": blogs, "alert": alert})


@router.get("/app/blog/{id}")
def blog_detail(request: Request, id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    return templates.TemplateResponse(
        "blog/detail.html", {"request": request, "blog": blog}
    )





