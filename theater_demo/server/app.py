#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate 
from models import db, Production, Role, Actor


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/productions')
def all_productions():
    q = Production.query.all()
    prod_list = [p.to_dict(only=('id', 'title', 'roles')) for p in q]

    res = make_response(jsonify(prod_list), 200)
    return res 

@app.route('/productions/<int:id>')
def production_by_id(id):
    q = Production.query.filter_by(id=id).first()

    prod_dict = q.to_dict()
    res = make_response(jsonify(prod_dict), 200)
    return res

# ✅ 1c. Create a `/roles` route to see the other side of the one-to-many relationship
@app.route('/roles')
def all_roles():
    query_all_roles = Role.query.all() 
    role_dict = [role.to_dict() for role in query_all_roles]
    return make_response(role_dict, 200)

@app.route('/actors')
def all_actors():
    query_all_actors = Actor.query.all() 
    actor_dict = [actor.to_dict() for actor in query_all_actors]
    return make_response(actor_dict, 200)

@app.route('/actors/<int:id>')
def actor_by_id(id):
    query_all_actors = Actor.query.filter_by(id=id).first() 
    
    return make_response(query_all_actors.to_dict(), 200)

# ✅ 3b. Create routes to access all actors and all productions
if __name__ == '__main__':
    app.run(port=5555, debug=True)