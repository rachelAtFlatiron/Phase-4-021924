# handle creating the database

#SQLAlchemy import
# the foundation of flask_sqlalchemy is SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()
# flask-sqlalchemy is our ORM
# it is Python that will be responsible for creating our tables, seeding, etc.
# a class/model will represent a table
# attributes will represent columns

# 1. ✅ Create a Production Model
#Production refers to the python class (that represents are sqlite table)
#create actual table in database (using model) via Flask Migrate (see app.py)
class Production(db.Model, SerializerMixin): 
    #sqlite table name
    __tablename__ = 'productions' 

    # each attribute aligns with a column 
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    title = db.Column(db.String)
    genre = db.Column(db.String)
    length = db.Column(db.Integer)
    year = db.Column(db.Integer) 
    image = db.Column(db.String)
    language = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String) 
    composer = db.Column(db.String)
    # ✅ 9b. Use serializer rules to remove `created_at` and `updated_at`
    # SERIALIZER RULE EXPECTS TUPLE 
    # IF YOU ONLY HAVE ONE THING IN YOUR TUPLE
    # DON'T FORGET THE TRAILING COMMA
    serialize_rules = ("-updated_at", "-created_at")

    def __repr__(self):
        return f'<Production id={self.id} title={self.title} />'

    
# ✅ 2. navigate to app.py