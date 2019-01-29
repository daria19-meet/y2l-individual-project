from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///cats.db?check_same_thread=False")
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_dancer(name, pic, age, nationality, company, styles, shows):
    dancer_object= Dancer(
    	name=name, 
    	pic=pic,
    	age=age, 
    	nationality=nationality, 
    	company=company, 
    	styles=styles, 
    	shows=shows)

    session.add(dancer_object)
    session.commit()

def add_dance(name, origin, history, moves):
    dance_object= Dance(
    	name=name, 
    	origin=origin, 
    	moves=moves, 
        history=history)

    session.add(dance_object)
    session.commit()

def add_studio(name, year, styles, location):
    studio_object= Studio(
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

def query_studio_by_name(name):
	return session.query(Studio).filter_by(name=name).first()

def query_dancer_by_styles(style):
	return session.query(Dancer).filter_by(styles=style).all()

def query_studio_by_style(style):
	return session.query(Studio).filter_by(styles=style).all()

def query_dancer_by_studio(studio):
	return session.query(Dancer).filter_by(company=studio).all()

def query_dancers():
	return session.query(Dancer).all()


add_dancer("Mikhail Baryshnikov", "bary.jpeg", "70",  "Russian-American","American Ballet Theatre", "Ballet", "Giselle, La Slyphide, Apollo, The Prodigal Son, Jewels, Opus 19/The Dreamer, Rhapsody")
add_dancer("Fred Astaire", "Fred-Astaire1.jpg", "Died at age 88", "American", "Fred Astaire Dance Studios", "Ballroom, Jazz, Tap", "Let's dance")
add_dancer("Michael Jackson", "jackson.jpg", "Died at age 51", "American", "Sony Music Records", "Pop, Disco", "Bad, Dangerous World Tour, HIStory World Tour, MJ & Friends, This is it" )
add_dancer("Anna Pavlova", "pavlova.jpg", "Died at age 49", "Russian", "Imperial Russian Ballet, Ballet Russes", "Ballet", "The Dying Swan, The False Dryads, The Sleeping Beauty, The Pharaohs Daughter")
add_studio("Bolshoi Ballet", "1776", "Moscow, Russia", "Ballet")
add_studio("The Royal Ballet", "1931", "Convent Garden, London, England", "Ballet")
add_studio("Debbie Reynolds Legacy Studio", "1976", "Los Angeles, California, US", "Pop, Ballet, Ballroom, Hip Hop, Disco, Contemporary, Lyrical, Acro, Tap, Jazz")
add_studio("Abby Lee Dance Company", "1983", "Pittsburgh, Pennslyvania", "Ballet, Jazz, Tap, Acro, Lyrical, Contemporary, Hip Hop")
add_dance("Hip-Hop", "New York","Late 1960's", "Running Man, The Worm, The Robot")
add_dance("Ballet", "Italy", "Fifteenth Century", "Plie, Assemble, Grand Jete")
add_dance("Jazz", "African Rituals", 'Early 20th Century', "Chasse, Jazz Walk")
add_dance("Contemporary", "Europe", "Mid Twenieth Century", "Muffintop-Less")
add_dance("Salsa", "Cuba", "1800s", "The Suave, The Rejection")
add_dance("Disco", "US", "Late 1970's", "YMCA, The Hustle")