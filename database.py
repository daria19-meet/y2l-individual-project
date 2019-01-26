from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_dancer(name, pic, age, nationality, studio, styles, shows):
    dancer_object= Dancer(
    	name=name, 
    	pic=pic,
    	age=age, 
    	nationality=nationality, 
    	studio=studio, 
    	styles=styles, 
    	shows=shows)

    session.add(dancer_object)
    session.commit()

def add_dance(name, origin, history, moves, performance, dancers):
    dance_object= Dancer(
    	name=name, 
    	origin=origin, 
    	moves=moves, 
    	performance=performance, 
    	history=history)

    session.add(dance_object)
    session.commit()

def add_studio(name, year, styles, location):
    studio_object= Dancer(
    	name=name, 
    	year=year, 
    	styles=styles, 
    	location=location)

    session.add(studio_object)
    session.commit()

def query_dancer_by_name(name):
	return session.query(Dancer).filter_by(name=name).first()

def query_dance_by_name(name):
	return session.query(Dance).filter_by(name=name).first()

def query_studio_by name(name):
	return session.query(Studio).filter_by(name).first()

def query_dancer_by_styles(style):
	return session.query(Dancer).filter_by(styles=style).all()

def query_studio_by_style(style):
	return session.query(Studio).filter_by(styles=style).all()

def query_dancer_by_studio(studio):
	return session.query(Dancer).filter_by(studio=studio).all()

def query_dancers():
	return session.query(Dancer).all()


if __name__ == "__main__":
	add_dance('Mikhail Baryshnikov', 'https://www.google.co.il/url?sa=i&source=images&cd=&ved=2ahUKEwiu-8Wm8YvgAhXRZVAKHVs2COMQjRx6BAgBEAU&url=https%3A%2F%2Fwww.thetimes.co.uk%2Farticle%2Fmikhail-baryshnikov-still-dancing-at-69-58vq8fv6p&psig=AOvVaw27gFypDduqwVu5nGfKOAR3&ust=1548607087617005', '70',  )
