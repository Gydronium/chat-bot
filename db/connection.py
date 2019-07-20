from peewee import BooleanField, IntegerField, Model, PostgresqlDatabase

db = PostgresqlDatabase(
    'mydb',  # Required by Peewee.
    user='postgres',  # Will be passed directly to psycopg2.
    password='1',  # Ditto.
    host='postgres://kxqgaprjxzbtqm:d77ed83f11ba731a5ca99019bf21780dde5e187f745e3e4c87bf22dab17e797f@ec2-54-243-47-196.compute-1.amazonaws.com:5432/d65m3tup9um7l4')  # Ditto.


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class User(BaseModel):
    id = IntegerField()
    is_boss = BooleanField()

    class Meta:
        table_name = 'user'
