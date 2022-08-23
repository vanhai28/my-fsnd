import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS,cross_origin
import sys

from utils.helpers import *
from models import Movie, Actor, MovieActor, db_drop_and_create_all, setup_db
from auth.auth import AuthError, requires_auth
from form import *

def create_app(test_config=None):
  db = SQLAlchemy()
  app = Flask(__name__)
  app.config.update(dict(
      SECRET_KEY="powerful secretkey",
      WTF_CSRF_SECRET_KEY="a csrf secret key"
  ))
  setup_db(app)
  CORS(app)
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})




      
  '''
  @TODO uncomment the following line to initialize the datbase
  !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
  !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
  !! Running this funciton will add one
  '''
  #db_drop_and_create_all()
  
  
  @app.route('/', methods=['GET'])
  def init():
    return jsonify({
              'success':True
          })
  # ROUTES
  '''
  @TODO implement endpoint
      GET /drinks
          it should be a public endpoint
          it should contain only the drink.short() data representation
      returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
          or appropriate status code indicating reason for failure
  '''

  @app.route('/api/movies', methods=['GET'])
  @cross_origin()
  @requires_auth("get:all-movie")
  def getMovies(self):
      try:
          data = db.session.query(Movie).all()
          listMovies = convertTableToList(data)

          movies = []

          for dict_movies in listMovies:
              movie = Movie(id=dict_movies['id'],title=dict_movies["title"], release_date=dict_movies["release_date"])
              movies.append(movie.value())

          return jsonify({
              'success':True,
              "movies": movies
          })
      except:
          print('error: ',sys.exc_info())
          abort(500)

  @app.route('/api/movies/<id>', methods=['GET'])
  @cross_origin()
  @requires_auth("get:movie")
  def getMoviesDetail(self,id):
  #def getMoviesDetail(id):
    data = db.session.query(Movie).filter(Movie.id == id).first()

    if(data is None):
      abort(404)

    return jsonify({
        'success':True,
        "movies": data.value()
    })


  @app.route('/api/movies', methods=['POST'])
  @cross_origin()
  @requires_auth("add:movie")
  def create_movies(self):
    movieForm = MovieForm()

    movie = Movie(
      title=movieForm.title.data,
      release_date=movieForm.release_date.data
    )
    if(not movieForm.title.data or not movieForm.release_date.data):
      abort(400)
    try:
      movie.insert()
    except:
      return jsonify({"success": False,'message': 'Error {0}'.format(sys.exc_info())})
    return jsonify({
        'success':True,
        "movies": movie.value()
    })

  @app.route('/api/movies/<id>', methods=['PUT'])
  @cross_origin()
  @requires_auth("edit:movie")
  def edit_movies(self, id:int):
  #def edit_movies(id:int):
    movieForm = MovieForm(request.form)
    movie = Movie.query.filter(Movie.id == id).one_or_none()
    if(movie is None):
      abort(404)

    try:

      movie.title = movieForm.title.data
      movie.release_date = movieForm.release_date.data
      movie.update()
    except:
      return jsonify({"success": False,'message': '{0}'.format(sys.exc_info())})
    return jsonify({
        'success':True,
        "movies": movie.value()
    })
  @app.route('/api/movies/<id>', methods=['DELETE'])
  @cross_origin()
  @requires_auth("delete:movie")
  def delete_movies(self,id):
  #def delete_movies(id):
    movie = Movie.query.filter(Movie.id == id).one_or_none()
    if(movie is None):
      abort(400)

    try:
      movie.delete()
    except:
      return jsonify({"success": False,'message': '{0}'.format(sys.exc_info())})
    return jsonify({
        'success':True
    })


  @app.route('/api/actors', methods=['GET'])
  @cross_origin()
  @requires_auth("get:all-actor")
  def getActors(self):
      try:
          data = db.session.query(Actor).all()
          listActors = convertTableToList(data)

          actors = []

          for dict_actors in listActors:
              actor = Actor(id=dict_actors['id'],name=dict_actors["name"], age=dict_actors["age"])
              actors.append(actor.value())

          return jsonify({
              'success':True,
              "actors": actors
          })
      except:
          print('error: ',sys.exc_info())
          abort(500)

  @app.route('/api/actors/<id>', methods=['GET'])
  @cross_origin()
  @requires_auth("get:actor")
  def getActorsDetail(self,id):
  #def getActorsDetail(id):
    data = db.session.query(Actor).filter(Actor.id == id).first()
    if(data is None):
      abort(404)
    return jsonify({
        'success':True,
        "actors": data.value()
    })

  @app.route('/api/actors', methods=['POST'])
  @cross_origin()
  @requires_auth("add:actor")
  def create_actors(self):
    actorForm = ActorForm(request.form)

    if not actorForm.name.data or not actorForm.age.data:
      abort(400)

    actor = Actor(
      name=actorForm.name.data,
      age=actorForm.age.data
    )
    try:
      actor.insert()
    except:
      return jsonify({"success": False,'message': 'Error {0}'.format(sys.exc_info())})
    return jsonify({
        'success':True,
        "actors": actor.value()
    })

  @app.route('/api/actors/<id>', methods=['PUT'])
  @cross_origin()
  @requires_auth("edit:actor")
  def edit_actors(self,id):
  #def edit_actors(id):
    actorForm = ActorForm(request.form)
    actor = Actor.query.filter(Actor.id == id).one_or_none()

    if(actor is None):
      abort(400)
    try:
      actor.name = actorForm.name.data
      actor.age = actorForm.age.data
      actor.update()
    except:
      return jsonify({"success": False,'message': 'Error {0}'.format(sys.exc_info())})
    return jsonify({
        'success':True,
        "actors": actor.value()
    })

  @app.route('/api/actors/<id>', methods=['DELETE'])
  @cross_origin()
  @requires_auth("delete:actor")
  def delete_actors(self, id:int):
  #def delete_actors(id:int):
    actor = Actor.query.filter(Actor.id == id).one_or_none()

    if(actor is None):
      abort(400)
    try:
      actor.delete()
    except:
      return jsonify({"success": False,'message': 'Error {0}'.format(sys.exc_info())})
    return jsonify({
        'success':True
    })

  @app.route('/api/movies/actors', methods=['POST'])
  @cross_origin()
  @requires_auth("add:actor-to-movie")
  def add_actors_to_movie(self):
    form = MovieActorForm(request.form)

    if not form.actor_id.data or not form.movie_id.data:
      abort(400)

    movieActor = MovieActor(
      actor_id=form.actor_id.data,
      movie_id=form.movie_id.data
    )
    try:
      movieActor.insert()
    except:
      return jsonify({"success": False,'message': 'Error {0}'.format(sys.exc_info())})
    return jsonify({
        'success':True
    })



  # Error Handling
  '''
  error handling for unprocessable entity
  '''
  @app.errorhandler(422)
  def handle_unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable"
      }), 422

  '''
  error handling for Unauthorized 
  '''
  @app.errorhandler(401)
  def hanle_Unauthorized (error):
      return jsonify({
          "success": False,
          "error": 401,
          "message": "Unauthorized !"
      }), 401
  '''
  error handling for bad request
  '''
  @app.errorhandler(400)
  def handle_badRequest(error):
      return jsonify({
          "success": False,
          "error": 400,
          "message": "Bad request!"
      }), 400
  '''
  error handling for server error
  '''
  @app.errorhandler(500)
  def handle_badRequest(error):
      return jsonify({
          "success": False,
          "error": 500,
          "message": "Something went wrong!"
      }), 500


  '''
  @ implement error handler for 404
  '''
  @app.errorhandler(404)
  def handle_not_found_error(e):
      return jsonify({
                  "success": False,
                  "error": 404,
                  "message": "resource not found"
                  }), 404
  app.register_error_handler(404, handle_not_found_error)
  '''
  @ implement error handler for AuthError
  '''
  @app.errorhandler(AuthError)
  def handle_auth_error(ex):
      response = jsonify(ex.error)
      response.status_code = ex.status_code
      return response
  
  return app

app = create_app()

if __name__ == '__main__':
    app.run()