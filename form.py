from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateField, IntegerField
from wtforms.validators import DataRequired, Optional, URL

class MovieForm(FlaskForm):
    id = IntegerField(
        'id'
    )
    title = StringField(
        'title',
        validators=[DataRequired()]
    )
    release_date = StringField(
        'release_date',
        validators=[DataRequired()]
    )

class ActorForm(FlaskForm):
    id = IntegerField('id')
    name = StringField(
        'name',
        validators=[DataRequired()]
    )
    age = IntegerField(
        'age',
        validators=[DataRequired()]
    )
class MovieActorForm(FlaskForm):
    id = IntegerField('id')
    actor_id = IntegerField(
        'actor_id',
        validators=[DataRequired()]
    )
    movie_id = IntegerField(
        'movie_id',
        validators=[DataRequired()]
    )