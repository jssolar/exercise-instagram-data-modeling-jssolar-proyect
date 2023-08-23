import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base() # declaracion de la base de sqlAlchemy
# Base, es una clase de python, que permite heredarle metodos, caracteristicas (clase principal)  a las clases que creemos.

class User(Base):
    __tablename__ = 'user' #--creacion nombre de tabla. debe ser en minúscula y singular, por regla gral--#
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String, nullable=False, unique=True)
    comment = relationship("Comment")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(600), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id')) 
    author_id = Column(Integer, ForeignKey('user.id'))
   

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_id = (Integer) 
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    tipo = Column(String(30))
    url= Column(String(200))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post) 


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column( Integer, ForeignKey('user.id'))


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
