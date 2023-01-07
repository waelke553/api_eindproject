from pydantic import BaseModel


class LandBase(BaseModel):
    name: str


class LandCreate(LandBase):
    pass


class Land(LandBase):
    id: int

    class Config:
        orm_mode = True




class SchoolBase(BaseModel):
    name: str
    land_id: int

class SchoolCreate(SchoolBase):
    pass

class School(SchoolBase):
    id: int

    class Config:
        orm_mode = True





class UserBase(BaseModel):
    name: str
    school_id: int

class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserEdit(BaseModel):
    name: str