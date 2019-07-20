from peewee import BooleanField, IntegerField, Model, PostgresqlDatabase

db = PostgresqlDatabase(
    'mydb',  # Required by Peewee.
    user='postgres',  # Will be passed directly to psycopg2.
    password='1',  # Ditto.
    host='127.0.0.1')  # Ditto.


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class User(BaseModel):
    id = IntegerField()
    is_boss = BooleanField()

    class Meta:
        table_name = 'user'
