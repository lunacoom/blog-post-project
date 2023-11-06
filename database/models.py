from peewee import Model, CharField, BooleanField, SqliteDatabase, TextField, IntegerField, DateField
from datetime import datetime


dt = SqliteDatabase('site.db')


class Users(Model):
    name = CharField(max_length=150)
    username = CharField(max_length=150, unique=True)
    password = CharField(max_length=150)
    status = BooleanField(default=False)
    
    class Meta:
        db_name = 'users'
        database = dt


class Articles(Model):
    title = CharField(max_length=150)
    description = TextField()
    views = IntegerField(default=0)
    photo = CharField(max_length=200)
    created_at = DateField(default=datetime.now)
    
    class Meta:
        db_name = 'articles'
        database = dt


Users.create_table()
Articles.create_table()

