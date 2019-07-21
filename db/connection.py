from peewee import BooleanField, IntegerField, Model, PostgresqlDatabase

db = PostgresqlDatabase(
    'dd35r2lke50gae',  # Required by Peewee.
    user='collopkaitptzu',  # Will be passed directly to psycopg2.
    password='c4d225ab82ed202dfecdc82f9bebc1e4bd06ef7f3673c55b541fb707a6fc7c61',  # Ditto.
    host='ec2-174-129-41-127.compute-1.amazonaws.com')  # Ditto.


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class User(BaseModel):
    id = IntegerField()
    is_boss = BooleanField()

    class Meta:
        table_name = 'vk_user'
