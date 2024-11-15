import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column()
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Character(Base):
        __tablename__ = 'character'
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        gender = Column(String(250), nullable=False)
        eye_color = Column(String(250), nullable=False)
        hair_color = Column(String(250), nullable=False)



class Planet(Base):
        __tablename__ = 'planet'
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        population = Column(Integer)
        terrain = Column(String(250), nullable=False)

        



class Favorite(Base):
        __tablename__ = 'favorite'
        id = Column(Integer, primary_key=True)
        favorite_planet = Column(String(250))
        favorite_people = Column(String(250))
        user_to_fav = Column(Integer, ForeignKey('user.id')) 
        user_to_fav_planet = Column(Integer, ForeignKey('planet.id'))
        user_to_fav_char = Column(Integer, ForeignKey('character.id')) 
        user = relationship(User)
        character = relationship(Character)
        planet = relationship(Planet)











def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
