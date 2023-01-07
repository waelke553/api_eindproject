from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# #"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500",
    "http://waelke553.github.io",
    "https://waelke553.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/land/", response_model=schemas.Land)
def create_land(land: schemas.LandCreate, db: Session = Depends(get_db)):
    db_land = crud.get_land_by_name(db, name=land.name)
    if db_land:
        raise HTTPException(status_code=400, detail="Land already registered")
    return crud.create_land(db=db, land=land)

@app.get("/land/", response_model=list[schemas.Land])
def get_landen(db: Session = Depends(get_db)):
    landen = crud.get_land(db)
    return landen

@app.get("/land/{land_id}", response_model=schemas.Land)
def read_land(land_id: int, db: Session = Depends(get_db)):
    db_land = crud.get_land_by_id(db, land_id=land_id)
    if db_land is None:
        raise HTTPException(status_code=404, detail="Land not found")
    return db_land


@app.post("/school/", response_model=schemas.School)
def create_school(school: schemas.SchoolCreate, db: Session = Depends(get_db)):
    db_school = crud.get_school_by_name(db, name=school.name)
    if db_school:
        raise HTTPException(status_code=400, detail="School already registered")
    return crud.create_school(db=db, school=school)

@app.get("/school/", response_model=list[schemas.School])
def get_schools(db: Session = Depends(get_db)):
    school = crud.get_school(db)
    return school

@app.get("/school/{school_id}", response_model=schemas.School)
def read_school(school_id: int, db: Session = Depends(get_db)):
    db_school = crud.get_school_by_id(db, school_id=school_id)
    if db_school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return db_school







@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db=db, user=user)



@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/")
def delete_the_user(user: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user)
    if db_user:
        crud.delete_user(db=db, name=user)
        return {"detail": "User has being deleted"}
    else:
        raise HTTPException(status_code=400, detail="User isn't registered")

@app.put("/users/{user_id}")
def change_the_user(user_id: int, name: schemas.UserEdit, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user:
        return crud.change_user(db, name, user_id)
    else:
        raise HTTPException(status_code=400, detail="User-ID isn't registered")