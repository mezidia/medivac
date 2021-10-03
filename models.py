from operator import pos
from peewee import Model, CharField, PrimaryKeyField, IntegerField, ForeignKeyField, FloatField
from peewee import Proxy

database_proxy = Proxy()

# It is for an example
class User(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()
    age = IntegerField()
    gender = CharField()
    nationality = CharField()


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField(unique=True)

    class Meta:
        database=database_proxy
        order_by='id'


class Car(BaseModel):
    class Meta:
        db_table='cars'


class Place(BaseModel):
    class Meta:
        db_table='places'


class Route(BaseModel):
    place_from = ForeignKeyField(Place, field='name')
    place_to = ForeignKeyField(Place, field='name')
    price = FloatField()
    car = ForeignKeyField(Car, field='id')

    class Meta:
        db_table='routes'
