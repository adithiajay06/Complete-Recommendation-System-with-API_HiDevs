from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience_level = Column(String)

    skills = relationship("Skill", back_populates="user")
    interactions = relationship("Interaction", back_populates="user")


class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    category = Column(String)
    difficulty = Column(String)
    popularity_score = Column(Float)

    interactions = relationship("Interaction", back_populates="content")


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    skill_name = Column(String)

    user = relationship("User", back_populates="skills")


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content_id = Column(Integer, ForeignKey("content.id"))
    interaction_type = Column(String)
    rating = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="interactions")
    content = relationship("Content", back_populates="interactions")