# Backend - CAPSTONE PROJECT

## Setting up the Backend

### Install Dependencies

1. **Python 3.10** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Run the Server
install libraries
```bash
pip install -r requirements.txt
```
From within the `./src` directory first ensure you are working using your created virtual environment.
Notify that remove comment this line in app.py in IN THE FIRST TIME run locall to build database 
```bash
 #db_drop_and_create_all()
 ```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.
## HEROKU LINK: https://fsnd-movie-app.herokuapp.com/

## For role Casting_Assistant

CASTING_ASSISTANT_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJ5cWlIZUFpSGFqRHh6Y3ZxQllKZyJ9.eyJpc3MiOiJodHRwczovL2Rldi04MmZwZG0zeS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTc3MDM4NzQ0NDAzNjA5ODM5NzIiLCJhdWQiOiJodHRwczovY2FzdGluZy9hcGkiLCJpYXQiOjE2NjEyNjYzNDUsImV4cCI6MTY2MTM1Mjc0NSwiYXpwIjoicWFLUTFJOU04dFg2N0RnMVlndTdZTXZvak52VmJ1RHAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvciIsImdldDphbGwtYWN0b3IiLCJnZXQ6YWxsLW1vdmllIiwiZ2V0Om1vdmllIl19.HQo8MBHKurGJOcHu_5wLTKw7Bjqj7dAu5cpEbBDp9k-tiKrr43BPOdHqLIPu7bLYkG_DrFtYPlAfraGmAdSU_t32ySXSXOBmk-ROJrClNObO_DkNpho7taxvg30H_lJlz6eSIVIePRVanblz09puBDESNPrggusErNjy4LUVD3vh-SHebyOOrxKoQDOlLg80RcJ6PDMNZV3qJ2UbMQqKjFBWtFuVTWNH9Uo1dHTBnt4495YASwOhvR6Z9wD_gDWrjIv8CffVi-YjJWj8PUblGpv55BpDt1--QX3Y2XJMuX2hHsZ0hfTrXNK0oXlE7G5UFl66JsVvuCqd00sy_6PaIA"

## For role Casting Director
CASTING_DIRECT_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJ5cWlIZUFpSGFqRHh6Y3ZxQllKZyJ9.eyJpc3MiOiJodHRwczovL2Rldi04MmZwZG0zeS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDkwNTYxNzA4NzA2NzU3Nzc3MjAiLCJhdWQiOiJodHRwczovY2FzdGluZy9hcGkiLCJpYXQiOjE2NjEyNjY2MTgsImV4cCI6MTY2MTM1MzAxOCwiYXpwIjoicWFLUTFJOU04dFg2N0RnMVlndTdZTXZvak52VmJ1RHAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDphY3Rvci10by1tb3ZpZSIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0OmFsbC1hY3RvciIsImdldDphbGwtbW92aWUiLCJnZXQ6bW92aWUiXX0.opvzGQKxiyc6aMguXdA8kZcNpz-9ApjrGfc1oL-QOrUHPzHMCHbjspimSSKPD1yDjktp6n2D1EQgu0g_8hQYJCjWO22fJV929FYkJzWQ9VWoAL1_Sg46Z6gyxrtDbzLf58GbSUmXW3_xHybJsst6xD8wiHevm_2xiRJOG4ObvnSpGB-wJgUfXrenFZm-WriZrHlFs4Z8LcTqWrQG6SL9TsGTjnQEvMY5Pm7AQggQEZFL51NQK6JykgW7jdypxqTSl7wI5PNs-O8XFb3iu6Mom5whrQE40GKce0cJ5f4BpmhqFllY5RJmVe6_CRFiyvTx3MhGA7GnQr6UGfFZ7X2ThA"

## For role Executive Producer
EXECUTIVE_PRODUCER_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJ5cWlIZUFpSGFqRHh6Y3ZxQllKZyJ9.eyJpc3MiOiJodHRwczovL2Rldi04MmZwZG0zeS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDE5ODMzMTI5NTM0MjUxMTE0NTAiLCJhdWQiOiJodHRwczovY2FzdGluZy9hcGkiLCJpYXQiOjE2NjEyNjY1NTMsImV4cCI6MTY2MTM1Mjk1MywiYXpwIjoicWFLUTFJOU04dFg2N0RnMVlndTdZTXZvak52VmJ1RHAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDphY3Rvci10by1tb3ZpZSIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0OmFsbC1hY3RvciIsImdldDphbGwtbW92aWUiLCJnZXQ6bW92aWUiXX0.Xi5H6czkqd2_G8Baw1rByj1mJLE0z2Hmx7_wDsV3oWRwqofPS8aX9yrWlOhW5M41RxdeGK_hePXOuyI7lhnnELGcqMmAQ1YefqBa5O8Sqgc0hldpHGNcg-0PLqU2asf7QOKi3gDbiEe-99o3VMBvgozOPoKpjezFka5CgseZuCyG-YRjnID3q8ljYZ1qg0xvY0FsYSVseraVTO8F30VEAyEZ3h6_B-gpMtNzCA-vRWoi8Pnnwm-PvWvMe5eMdxOZBhnc_g5mwAbfwHZvZoPVLdJdQurSDiM-HomMtleia2yNWMX_LWu8EXmrMLn8sRuf00fpHxGBNoLb77LACXEjNw"



## To RUN test_app
In app.py, for each router, comment the following line `@requires_auth(...)`.
if the function has `self` arguments, remove it. (just for testing.)
Ex: ` def getMoviesDetail(self,id):` to `def getMoviesDetail(id):`
After run file test_app, you can discard change to run normally

## To RUN on Postman
Please use file `udacity-fsnd-udaspicelatte.postman_collection` to quickly import the postman collection.
You can use `token` for each role I saved in file readme.md (the beginning of this file)

## To RUN with Heroku api
Doing similar to run on postman locally, just change host to link heroku `https://fsnd-movie.herokuapp.com/`. 
Cause heroku sleep if the app does not having access in amounts of time, so please call api again if fail in the first time.

## Documenting the Endpoints

`GET '/api/movies'`

- Fetches all the movies in database
- Request Arguments: None
- Returns: An object with a single key, `movies`, that contains an object of key: value pairs.

```json
{
    "movies": [
        {
            "actors": [
                {
                    "age": 20,
                    "id": 1,
                    "name": "Anna"
                }
            ],
            "id": 1,
            "release_date": "Fri, 08 Oct 2010 17:00:00 GMT",
            "title": "The king of the rings"
        }
    ],
    "success": true
}
```

`GET '/api/movies/<id>'`

- Fetches one the movies in database 
- Request Arguments: id: integer
- Returns: An object with a single key, `movies`, that contains an object of key: value pairs.

```json
{
    "movies": {
        "actors": [
            {
                "age": 20,
                "id": 1,
                "name": "Anna"
            }
        ],
        "id": 1,
        "release_date": "Fri, 08 Oct 2010 17:00:00 GMT",
        "title": "The king of the rings"
    },
    "success": true
}
```


`POST '/api/movies'`

- edit one the movies in database 
- Request Arguments: None
- The payload like:
```json
{
  "title": "The name of movie",
  "release_date": "2000-10-12"
}
```
- Returns: An object with a single key, `movies`, that contains an object of key-value pairs of the movie edited

```json
{
    "movies": {
        "actors": [
            {
                "age": 20,
                "id": 1,
                "name": "Anna"
            }
        ],
        "id": 1,
        "release_date": "Wed, 11 Oct 2000 17:00:00 GMT",
        "title": "The name of movie"
    },
    "success": true
}
```

`PUT '/api/movies/<id>'`

- edit one the movies in database 
- Request Arguments: id: integer
- The payload like:
```json
{
  "title": "The king of moon",
  "release_date": "2000-10-12"
}
```
- Returns: An object with a single key, `movies`, that contains an object of key-value pairs of the movie edited

```json
{
    "movies": {
        "actors": [
            {
                "age": 20,
                "id": 1,
                "name": "Anna"
            }
        ],
        "id": 1,
        "release_date": "Wed, 11 Oct 2000 17:00:00 GMT",
        "title": "The king of moon"
    },
    "success": true
}
```


`DELETE '/api/movies/add/actor'`

- edit one the movies in database 
- Request Arguments: id: integer
- The payload like:
```json
{
  "movie_id": 1,
  "actor_id": 1
}
```
- Returns: An object with the result of request

```json
{
    "success": true
}
```
`DELETE '/api/movies/<id>'`

- edit one the movies in database 
- Request Arguments: id: integer
- Returns: An object with the result of request

```json
{
    "success": true
}
```




`GET '/api/actors'`

- Fetches all the actors in database
- Request Arguments: None
- Returns: An object with a single key, `movies`, that contains an object of key: value pairs.

```json
{
    "actors": [
        {
            "age": 22,
            "id": 1,
            "movies": [
                {
                    "id": 1,
                    "release_date": "Wed, 11 Oct 2000 17:00:00 GMT",
                    "title": "The king of moon"
                }
            ],
            "name": "Bob"
        },
        {
            "age": 22,
            "id": 2,
            "movies": [],
            "name": "Bob"
        }
    ],
    "success": true
}
```

`GET '/api/actors/<id>'`

- Fetches one the actor in database 
- Request Arguments: id: integer
- Returns: An object with a key `actors`, that contains an object of key: value pairs.

```json
{
    "actors": {
        "age": 22,
        "id": 1,
        "movies": [
            {
                "id": 1,
                "release_date": "Wed, 11 Oct 2000 17:00:00 GMT",
                "title": "The king of moon"
            }
        ],
        "name": "Bob"
    },
    "success": true
}
```


`POST '/api/actors'`

- Add new actor to database 
- Request Arguments: None
- The payload like:
```json
{
  "name": "Anna",
  "age": "20"
}
```
- Returns: An object with a key `actors`, that contains an object of key-value pairs of the actor added to the database

```json
{
    "actors": {
        "age": 20,
        "id": 1,
        "movies": [
            {
                "id": 1,
                "release_date": "Wed, 11 Oct 2000 17:00:00 GMT",
                "title": "The king of moon"
            }
        ],
        "name": "Anna"
    },
    "success": true
}
```

`PUT '/api/actors/<id>'`

- Edit one the actors in database 
- Request Arguments: id: integer
- The payload like:
```json
{
  "name": "Bob",
  "age": "25"
}
```
- Returns: An object with a key `actors`, that contains an object of key-value pairs of the actor edited

```json
{
    "actors": {
        "age": 22,
        "id": 1,
        "movies": [
            {
                "id": 1,
                "release_date": "Wed, 11 Oct 2000 17:00:00 GMT",
                "title": "The king of moon"
            }
        ],
        "name": "Bob"
    },
    "success": true
}
```


`DELETE '/api/actors/<id>'`

- Delete one the actor in database 
- Request Arguments: id: integer
- Returns: An object with the result of request

```json
{
    "success": true
}
```