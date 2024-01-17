from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from backend.db.session import get_db
from backend.db.repository.blog import list_blogs


templates = Jinja2Templates(directory="backend/templates")
router = APIRouter()


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return templates.TemplateResponse("blog/home.html", {"request": request, "blogs": blogs})
