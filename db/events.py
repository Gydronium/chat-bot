from peewee import BooleanField, IntegerField, DateTimeField, TextField, Model, PostgresqlDatabase

db = PostgresqlDatabase(
    'd7d2j8dntrcove',  # Required by Peewee.
    user='vmhedmdxwebeje',  # Will be passed directly to psycopg2.
    password='3be9848d492615f095e6821fec5499cc619c65ba446a6e84b63cf11ec17490ad',  # Ditto.
    host='ec2-107-21-120-104.compute-1.amazonaws.com')  # Ditto.


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class User(BaseModel):
    id = IntegerField()
    date = DateTimeField()
    message = TextField()
    is_upcoming = BooleanField()

    class Meta:
        table_name = 'events'


def insert_event(event_id, event_date, event_message, event_is_upcoming):
    User.insert(id=event_id, date=event_date, message=event_message, is_upcoming=event_is_upcoming).execute()


def get_all_events():
    return User.select()