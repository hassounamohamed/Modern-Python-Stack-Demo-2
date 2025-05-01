#Start FastAPI Application
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated

#app = FastAPI()

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]


#Create PostgreSQL connection
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL string for the Postgres database
# In this example, the database name is 'quizApp'
URL_DATABASE = 'postgresql://root@localhost:5432/quizApp'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Create PostgreSQL Tables
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)

class Choices(Base):
    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))


#Connect FastAPI, PostgreSQL with SQLAlchemy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#FastAPI Add Question Endpoint
# We passing in a data validation to validate the body of the API request
# and passing the database connection
@app.post('/questions/')
def create_questions(question: QuestionBase, db: db_dependency):
    # Here we use SQL Alchemy to write an ORM statement that will link with the database
    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = models.Choices(choice_text=choice.choice_text, is_correct=choice.is_correct, question_id=db_question.id)
        db.add(db_choice)
    db.commit()