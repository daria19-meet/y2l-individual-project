from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Dancer(Base):
    __tablename__= 'dancers'
    id=Column(Integer, primary_key=True)
    name= Column(String)
    pic=Column(String)
    age=Column(String)
    nationality= Column(String)
    studio=Column(String)
    styles=Column(String)
    shows=Column(String)


class Dance(Base):
	__tablename__='dance'
	id=Column(Integer, primary_key=True)
	name=Column(String)
	origin=Column(String)
	history= Column(String)
	moves=Column(String)
	performance=Column(String)

class Studio(Base):
	__tablename__='studio'
	id=Column(Integer, primary_key=True)
	name=Column(String)
	year=Column(Integer)
	location=Column(String)
	styles=Column(String)
