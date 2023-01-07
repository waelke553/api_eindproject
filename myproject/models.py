from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class School(Base):
    __tablename__ = "scholen"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    land_id = Column(Integer, ForeignKey("lands.id"))

    land_relation = relationship("Land", back_populates="school_relation")
    
    users_relation = relationship("User", back_populates="school_relation")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    school_id = Column(Integer, ForeignKey("scholen.id"))
    
    school_relation = relationship("School", back_populates="users_relation")


class Land(Base):
    __tablename__ = "lands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    school_relation = relationship("School", back_populates="land_relation")