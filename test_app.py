
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()
from app import create_app
from models import *

CASTING_ASSISTANT_TOKEN = os.getenv('CASTING_ASSISTANT_TOKEN', '')
CASTING_DIRECT_TOKEN = os.getenv('CASTING_DIRECT_TOKEN', '')
EXECUTIVE_PRODUCER_TOKEN = os.getenv('EXECUTIVE_PRODUCER_TOKEN', '')

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        
        self.newActor={
            "name": "Anna",
            "age":18
        }
        self.oldActor={
            "id": 1,
            "name": "Anna",
            "age":18
        }
        self.badActor={
            "name": "Anna"
        }

        self.newMovie={
            "title": "One Piece",
            "release_date": "2015-08-12"
        }
        self.oldMovie={
            "id": 10,
            "title": "One Piece",
            "release_date": "2015-08-12"
        }
        self.badMovie={
            "release_date": "2015-08-12"
        }

        self.movieActor={
            "actor_id": 1,
            "movie_id": 1,
        }
        self.badMovieActor={
            "actor_id": 1
        }
        self.headersNoneToken = {"Authorization": "Bearer"}
        self.headersAssistant = {"Authorization": "Bearer {0}".format(CASTING_ASSISTANT_TOKEN)}
        self.headersDirect = {"Authorization": "Bearer {0}".format(CASTING_DIRECT_TOKEN)}
        self.headersProducer = {"Authorization": "Bearer {0}".format(EXECUTIVE_PRODUCER_TOKEN)}
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_all_movies(self):
        res = self.client().get('/api/movies', headers=self.headersAssistant)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["movies"]))

    def test_get_all_movies_failed(self):
        res = self.client().get('/api/movies-failed', headers=self.headersAssistant)
        self.assertEqual(res.status_code, 404)

    def test_get_all_movies_401(self):
        res = self.client().get('/api/movies', headers=self.headersNoneToken)
        self.assertEqual(res.status_code, 401)
    

    def test_get_one_movies(self):
        res = self.client().get('/api/movies/1', headers=self.headersDirect)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_get_one_movies_failed(self):
        res = self.client().get('/api/movies/-1', headers=self.headersAssistant)
        self.assertEqual(res.status_code, 404)

    def test_get_one_movies_401(self):
        res = self.client().get('/api/movies/1', headers=self.headersNoneToken)
        self.assertEqual(res.status_code, 401)
    

    def test_add_one_movies(self):
        res = self.client().post('/api/movies',  data=self.newMovie, headers=self.headersDirect)
        self.assertEqual(res.status_code, 200)

    def test_add_one_movies_failed(self):
        res = self.client().post('/api/movies', data=self.badMovie, headers=self.headersDirect)
        self.assertEqual(res.status_code, 400)

    def test_add_one_movies_failed(self):
        res = self.client().post('/api/movies', data=self.badMovie)
        self.assertEqual(res.status_code, 401)

    def test_put_one_movies(self):
        res = self.client().put('/api/movies/10', data=self.oldMovie, headers=self.headersDirect)
        self.assertEqual(res.status_code, 200)

    def test_put_one_movies_failed(self):
        res = self.client().put('/api/movies/-1', data=self.oldMovie, headers=self.headersDirect)
        self.assertEqual(res.status_code, 404)

    def test_put_one_movies_401(self):
        res = self.client().put('/api/movies/1', data=self.oldMovie)
        self.assertEqual(res.status_code, 401)

    def test_put_one_movies_403(self):
        res = self.client().put('/api/movies/1', data=self.oldMovie, headers=self.headersAssistant)
        self.assertEqual(res.status_code, 403)

    def test_add_actor_to_movies(self):
        res = self.client().post('/api/movies/actors', data=self.movieActor, headers=self.headersProducer)
        self.assertEqual(res.status_code, 200)


    def test_add_actor_to_movie_401(self):
        res = self.client().post('/api/movies/actors', json=self.movieActor)
        self.assertEqual(res.status_code, 401)

    def test_add_actor_to_movie_403(self):
        res = self.client().post('/api/movies/actors', json=self.movieActor, headers=self.headersAssistant)
        self.assertEqual(res.status_code, 403)

    def test_delete_one_movies(self):
        res = self.client().delete('/api/movies/1', headers=self.headersProducer)
        self.assertEqual(res.status_code, 200)

    def test_delete_one_movies_failed(self):
        res = self.client().delete('/api/movies/-1', headers=self.headersProducer)
        self.assertEqual(res.status_code, 400)

    def test_delete_one_movies_401(self):
        res = self.client().delete('/api/movies/-1')
        self.assertEqual(res.status_code, 401)

    def test_delete_one_movies_403(self):
        res = self.client().delete('/api/movies/-1', headers=self.headersDirect)
        self.assertEqual(res.status_code, 403)


    def test_get_all_actor(self):
        res = self.client().get('/api/actors', headers=self.headersDirect)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_get_all_actor_404(self):
        res = self.client().get('/api/actors-failed', headers=self.headersDirect)
        self.assertEqual(res.status_code, 404)

    def test_get_all_actor_401(self):
        res = self.client().get('/api/actors')
        self.assertEqual(res.status_code, 401)
    
    
    def test_get_one_actors(self):
        res = self.client().get('/api/actors/1', headers=self.headersDirect)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_get_one_actors_404(self):
        res = self.client().get('/api/actors/-1', headers=self.headersDirect)
        self.assertEqual(res.status_code, 404)

    def test_get_one_actors_401(self):
        res = self.client().get('/api/actors/1')
        self.assertEqual(res.status_code, 401)
    

    def test_add_one_actors(self):
        res = self.client().post('/api/actors',  data=self.newActor, headers=self.headersDirect)
        self.assertEqual(res.status_code, 200)

    def test_add_one_actors_400(self):
        res = self.client().post('/api/actors', data=self.badActor, headers=self.headersDirect)
        self.assertEqual(res.status_code, 400)

    def test_add_one_actors_401(self):
        res = self.client().post('/api/actors', data=self.newActor)
        self.assertEqual(res.status_code, 401)

    def test_add_one_actors_403(self):
        res = self.client().post('/api/actors', data=self.newActor, headers=self.headersAssistant)
        self.assertEqual(res.status_code, 403)

    def test_put_one_actors(self):
        res = self.client().put('/api/actors/1', json=self.oldActor, headers=self.headersDirect)
        self.assertEqual(res.status_code, 200)

    def test_put_one_actors_400(self):
        res = self.client().put('/api/actors/-1', json=self.oldActor, headers=self.headersDirect)
        self.assertEqual(res.status_code, 400)

    def test_put_one_actors_401(self):
        res = self.client().put('/api/actors/1', json=self.oldActor)
        self.assertEqual(res.status_code, 401)

    def test_put_one_actors_403(self):
        res = self.client().put('/api/actors/1', json=self.oldActor, headers=self.headersAssistant)
        self.assertEqual(res.status_code, 403)

    def test_delete_one_actors(self):
        res = self.client().delete('/api/actors/1', headers=self.headersDirect)
        self.assertEqual(res.status_code, 200)

    def test_delete_one_actors_400(self):
        res = self.client().delete('/api/actors/-1', headers=self.headersDirect)
        self.assertEqual(res.status_code, 400)

    def test_delete_one_actors_401(self):
        res = self.client().delete('/api/actors/-1')
        self.assertEqual(res.status_code, 401)

    def test_delete_one_actors_403(self):
        res = self.client().delete('/api/actors/-1', headers=self.headersAssistant)
        self.assertEqual(res.status_code, 403)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()