from sqlalchemy.orm import Session
from backend.db.repository.blog import create_new_blog
from backend.schemas.blog import CreateBlog
from backend.tests.utils.user import create_random_user


def create_random_blog(db: Session):
    blog = CreateBlog(title="Test blog point", content="tests make the sistem stable")
    user = create_random_user(db=db)
    blog = create_new_blog(db=db, blog=blog, author_id=user.id)
    return blog



