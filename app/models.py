from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class Artist(db.Model):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    movie_id = Column(Integer, ForeignKey('movie.id'))


class Genre(db.Model):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    movie_id = Column(Integer, ForeignKey('movie.id'))


class Movie(db.Model):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    genres = relationship('Genre', backref='movies')
    artists = relationship('Artist', backref='movies')
