from sqlalchemy import Column, String, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI,pool_size=200, max_overflow=0)
Session = sessionmaker(bind = engine)
session = Session()

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

# ROUTES

'''
Movie
a persistent Movie entity, extends the base SQLAlchemy Model
'''


class Movie(db.Model):
    __tablename__ = 'Movie'
    # Autoincrementing, unique primary key
    id = db.Column(db.Integer, primary_key=True)
    # String Title
    title = db.Column(db.String(120))
    release_date = db.Column(db.Date)


    '''
    long()
        long form representation of the Movie model
    '''

    def value(self):
        actors = session.query(Actor)\
        .join(MovieActor, Actor.id == MovieActor.actor_id)\
        .filter(MovieActor.movie_id == self.id)\
        .all()

        list = []

        for _a in actors:
            list.append({
                'id': _a.id,
                'name': _a.name,
                'age': _a.age,
            })
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'actors': list 
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            Movie = Movie(title=req_title, recipe=req_recipe)
            Movie.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            Movie = Movie(title=req_title, recipe=req_recipe)
            Movie.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            Movie = Movie.query.filter(Movie.id == id).one_or_none()
            Movie.title = 'Black Coffee'
            Movie.update()
    '''

    def update(self):
        db.session.commit()

class Actor(db.Model):
    __tablename__ = 'Actor'
    # Autoincrementing, unique primary key
    id = db.Column(db.Integer, primary_key=True)
    # String name
    name = db.Column(db.String(120))
    age = db.Column(db.Integer)


    '''
    long()
        long form representation of the Movie model
    '''

    def value(self):
        movies = session.query(Movie)\
        .join(MovieActor, Movie.id == MovieActor.movie_id)\
        .filter(MovieActor.actor_id == self.id)\
        .all()
        
        listMovie = []

        for movie in movies:
            listMovie.append({
                'id': movie.id,
                'title': movie.title,
                'release_date': movie.release_date,
            })

        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'movies': listMovie
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            Actor = Actor(name=req_name, age=req_age)
            Actor.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            Actor = Actor(name=req_name, age=req_age)
            Actor.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            Actor = Actor.query.filter(Actor.id == id).one_or_none()
            Actor.name = 'Anna'
            Actor.update()
    '''

    def update(self):
        db.session.commit()



class MovieActor(db.Model):
    __tablename__ = 'MovieActor'
    # Autoincrementing, unique primary key
    id = db.Column(db.Integer, primary_key=True)
    # ID of the movie
    movie_id = db.Column(db.Integer, ForeignKey('Movie.id'))
    # ID of the actor
    actor_id = db.Column(db.Integer, ForeignKey('Actor.id'))


    '''
    long()
        long form representation of the Movie model
    '''

    def value(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'actor_id': self.actor_id,
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique id or null id
        EXAMPLE
            MovieActor = MovieActor(movie_id=movie_id, actor_id=actor_id)
            MovieActor.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            MovieActor.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            MovieActor = MovieActor.query.filter(MovieActor.id == id).one_or_none()
            MovieActor.movie_id = 1
            MovieActor.update()
    '''

    def update(self):
        db.session.commit()

