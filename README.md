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
## HEROKU LINK: https://fsnd-movie.herokuapp.com/

## For role Casting_Assistant

Casting_Assistant_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJ5cWlIZUFpSGFqRHh6Y3ZxQllKZyJ9.eyJpc3MiOiJodHRwczovL2Rldi04MmZwZG0zeS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTc3MDM4NzQ0NDAzNjA5ODM5NzIiLCJhdWQiOiJodHRwczovY2FzdGluZy9hcGkiLCJpYXQiOjE2NjEwMjU1MjIsImV4cCI6MTY2MTExMTkyMiwiYXpwIjoicWFLUTFJOU04dFg2N0RnMVlndTdZTXZvak52VmJ1RHAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvciIsImdldDphbGwtYWN0b3IiLCJnZXQ6YWxsLW1vdmllIiwiZ2V0Om1vdmllIl19.C3G7Ldz1qpf1mU2_-9ceoCaGwTk5oIc8Swo4pi6RwEMnp_Yk3WN2E10WuUuFlEwhpflyYx60lZfMXeKNal5nLOwUQE4gnm6AHqly8fF96vNrICjI0-yw1BdAgDnZzbIenCWeVcDkJEzD4VuBtElhNiAtFHcmoeX3A06zRrV9E6O16KGmvl_YwF0z5QAvCeNEnU7MCqXzPB8si5WqLRLbxE9UdWEg2V7c2Zhx_0BYB5mTcaPSbvZEw2DN1tlCcc0OPJzqGqF2gqerLl3OjHlyA4mqllRyhHTLwmiEjkdquVKLhYzZf2q4Dglss0v31QrSp1nOOmlBs77sHmXOPLL-YA
## For role Casting Director
Casting_Director_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJ5cWlIZUFpSGFqRHh6Y3ZxQllKZyJ9.eyJpc3MiOiJodHRwczovL2Rldi04MmZwZG0zeS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDkwNTYxNzA4NzA2NzU3Nzc3MjAiLCJhdWQiOiJodHRwczovY2FzdGluZy9hcGkiLCJpYXQiOjE2NjExNzIyNjAsImV4cCI6MTY2MTI1ODY2MCwiYXpwIjoicWFLUTFJOU04dFg2N0RnMVlndTdZTXZvak52VmJ1RHAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDphY3Rvci10by1tb3ZpZSIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0OmFsbC1hY3RvciIsImdldDphbGwtbW92aWUiLCJnZXQ6bW92aWUiXX0.WpXxk5oBA_vT2d19Z0kYilu-4pAIV4hbbcCs_SC3P08O4VpYBMjbZihFRCFbhHrWN7fXcixGJeH-HDz7a-QX35p832eJxIiQY4T7NaPiligvarUlXGEhd6Tp7k5Z3_oDbWjMXLzVVhDXon42dUgfzuQZLN7G-54m1qIsmyRY4WyFWuuTYLrnUzPa3FogRAxYbAqCclcdt_nVC9-MoxoKsCqDkXoo2BPEzGQAf6wcn13FzzASJSTRlQIKPr5bqxOSKv7Pq9y_PoKyBiwPdNdbNcvYN9ssDejZ9bveL3CidKftDkG0n7vUU7YiKeAKERH_Bjoo8OHv5_QnUNTk19znqQ

## For role Executive Producer
Executive_Producer_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJ5cWlIZUFpSGFqRHh6Y3ZxQllKZyJ9.eyJpc3MiOiJodHRwczovL2Rldi04MmZwZG0zeS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDE5ODMzMTI5NTM0MjUxMTE0NTAiLCJhdWQiOiJodHRwczovY2FzdGluZy9hcGkiLCJpYXQiOjE2NjEwMjU2MTIsImV4cCI6MTY2MTExMjAxMiwiYXpwIjoicWFLUTFJOU04dFg2N0RnMVlndTdZTXZvak52VmJ1RHAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDphY3Rvci10by1tb3ZpZSIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0OmFsbC1hY3RvciIsImdldDphbGwtbW92aWUiLCJnZXQ6bW92aWUiXX0.T6sAaE4BEwINpUb0HRbuiYE1dG2q1F-7V9gRllxZwKeARimPDjF9iOEADIph50DD_huQUFoy5W0OQKec5jmJo8elZN1rIG-wpsjPjLd7dHnVZW_2nnLTaYuhoi7ZtlJfKTo8xsyr0wFas7jzsJA0sMFWUd6tqJE3aniOFdG_IL0hNbTZseq2ejvfz1hTkWl96NS_tctapqanboxFE-eFCiCuYp1YOXSSWfnon7jZn7LFZ-07XsfkyE7RMBRAl9qlnpY2YDGKI5TZu8drzJ00LUlIaEHtotlrx74d9fiMSWOgd2oDoGKnPLBWM9BxLtWxUP4c9rbB_-K2QxSXLvczMA


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