from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from src.db import crud, models, schemas
from src.db.database import SessionLocal, engine
from src.utils.helpers import read_user_response, user_added_response

# API config
app = FastAPI()

origins = ['*']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*']
                   )

# Database config
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Routes

@app.get('/')
async def root():
    return {'status': True, 'message': 'API running...'}


@app.post("/bloom/add/")
def add(user: schemas.UserCreate, db: Session = Depends(get_db)):

    user_created = crud.create_user(db, user)

    return user_added_response(user_created)


@app.get("/blooam/users/")
def read_users(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/bloom/users/username/{username}")
def read_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=username)

    return read_user_response(db_user)
