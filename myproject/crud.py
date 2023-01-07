from sqlalchemy.orm import Session

import models
import schemas
import auth



def get_land(db: Session):
    return db.query(models.Land).all()

def get_land_by_id(db: Session, land_id: int):
    return db.query(models.Land).filter(models.Land.id == land_id).first()

def get_land_by_name(db: Session, name: str):
    return db.query(models.Land).filter(models.Land.name == name).first()

def create_land(db: Session, land: schemas.LandCreate):
    db_land = models.Land(name=land.name)
    db.add(db_land)
    db.commit()
    db.refresh(db_land)
    return db_land


def get_school(db: Session):
    return db.query(models.School).all()

def get_school_by_id(db: Session, school_id: int):
    return db.query(models.School).filter(models.School.id == school_id).first()

def get_school_by_name(db: Session, name: str):
    return db.query(models.School).filter(models.School.name == name).first()

def create_school(db: Session, school: schemas.SchoolCreate):
    db_school = models.School(name=school.name, land_id=school.land_id)
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school




def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.hashed_password)

    db_user = models.User(name=user.name, school_id=user.school_id, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, name: str):

    search = db.query(models.User).filter(models.User.name == name).first()
    db.delete(search)
    db.commit()
    return name

def change_user(db: Session, name=schemas.UserEdit, user_id = int):

    search = db.query(models.User).filter(models.User.id == user_id).first()
    search.name = name.name
    db.commit()
    db.refresh(search)
    return name

