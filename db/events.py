from peewee import BooleanField, IntegerField, DateTimeField, TextField, Model, PostgresqlDatabase

db = PostgresqlDatabase(
    'dd35r2lke50gae',  # Required by Peewee.
    user='collopkaitptzu',  # Will be passed directly to psycopg2.
    password='c4d225ab82ed202dfecdc82f9bebc1e4bd06ef7f3673c55b541fb707a6fc7c61',  # Ditto.
    host='ec2-174-129-41-127.compute-1.amazonaws.com')  # Ditto.


class BaseModel1(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class User1(BaseModel1):
    id = IntegerField()
    date = DateTimeField()
    message = TextField()
    is_upcoming = BooleanField()

    class Meta:
        table_name = 'events'


def insert_event(event_id, event_date, event_message, event_is_upcoming):
    User1.insert(id=event_id, date=event_date, message=event_message, is_upcoming=event_is_upcoming).execute()


def get_all_events():
    return User1.select()
