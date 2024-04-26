#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request, abort
from flask_migrate import Migrate 
from models import db, Production, Role, Actor
from flask_restful import Api, Resource
# 7a. import NotFound from werkzeug.exceptions and abort from Flask
from werkzeug.exceptions import NotFound, UnprocessableEntity, Unauthorized, NotAcceptable, MethodNotAllowed
# 10a. import UnprocessableEntity


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

migrate = Migrate(app, db)

api = Api(app)

db.init_app(app)

# | HTTP Verb 	|       Path       	| Description        	|
# |-----------	|:----------------:	|--------------------	|
# | GET       	|   /productions   	| READ all resources 	|
# | GET       	| /productions/:id 	| READ one resource   	|
# | POST      	|   /productions   	| CREATE one resource 	|
# | PATCH/PUT 	| /productions/:id 	| UPDATE one resource	|
# | DELETE    	| /productions/:id 	| DESTROY one resource 	|

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/productions', methods=["GET", "POST"])
def Productions():
    if(request.method=="GET"):
        # 7b. if not found, raise NotFound exception
        q = Production.query.all()
        prod_list = [p.to_dict() for p in q]
        res = make_response(jsonify(prod_list), 200)
        return res 
    
    if(request.method=="POST"):
        data = request.get_json()
        # 10b. if there's an exception, raise UnprocessableEntity
        prod = Production(title=data.get('title'), genre=data.get('genre'), length=data.get('length'), year=data.get('year'), image=data.get('image'), language=data.get('language'), director=data.get('director'), description=data.get('description'), composer=data.get('composer') )
        db.session.add(prod)
        db.session.commit()


        dict = prod.to_dict()
        return make_response(jsonify(dict), 201)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/productions/<int:id>', methods=["GET", "DELETE"])
def One_Production(id):
    if(request.method == 'GET'):
        q = Production.query.filter_by(id=id).first()
        # 7b. raise NotFound exception
        prod_dict = q.to_dict()
        res = make_response(jsonify(prod_dict), 200)
        return res

    if(request.method == "DELETE"):
        q = Production.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Roles(Resource):
    
    def get(self):
        q = Role.query.all()
        # 7c. If not found, use abort
        role_dict = [r.to_dict(only=('id', 'role_name', 'actor.name', 'production.title')) for r in q]
        return make_response(role_dict, 200)
    
    def post(self):
        data = request.get_json()
        # 10b. add unprocessable entity

        role = Role(role_name=data.get('role_name'), production_id=data.get('production_id'))
        db.session.add(role)
        db.session.commit()


        return make_response(role.to_dict(), 201)
    
api.add_resource(Roles, '/roles', '/test')

class One_Role(Resource):

    def get(self, id):
        q = Role.query.filter_by(id=id).first()
        if not q: 
            #return make_response({'mesage': 'make_response'}, 404)
            #raise NotFound('raise NotFound')
            #abort(404, 'aborting')
            raise NotFound('raising not found')
        # 7c. If not found, use abort
        return make_response(q.to_dict(), 200)
    def delete(self, id):
        q = Role.query.filter_by(id=id).first()
        if not q:
            raise NotFound
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)
    def patch(self, id):
        q = Role.query.filter_by(id=id).first()
        if not q:
            raise NotFound
        data = request.get_json()
        # 10b. raise unprocessable entity
        try:
            for attr in data:
                setattr(q, attr, data.get(attr))
            db.session.add(q)
            db.session.commit()
        except:
            raise UnprocessableEntity

        return make_response(q.to_dict(), 200)
    
api.add_resource(One_Role, '/roles/<int:id>')

# ~~~~~~~~~~~~~~~YOU DO~~~~~~~~~~~~~~~~~~~~
class Actors(Resource):
    def get(self):
        q = Actor.query.all()
        actor_dict = [a.to_dict() for a in q]
        return make_response(actor_dict, 200)
    
    def post(self):
        data = request.get_json()
        # 10b. raise unprocessable entity
        try:
            actor = Actor(name=data.get('name'), image=data.get('image'), age=data.get('age'), country=data.get('country'))
            db.session.add(actor)
            db.session.commit()
        except:
            abort(422, 'something went wrong')


        return make_response(actor.to_dict(), 201)
api.add_resource(Actors, '/actors')

class One_Actor(Resource):

    def get(self, id):
        q = Actor.query.filter_by(id=id).first()
        if not q:
            abort(404, "The Actor was not found")
        return make_response(q.to_dict(), 200)
    def delete(self, id):
        q = Actor.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)

    def patch(self, id):
        q = Actor.query.filter_by(id=id).first()
        data = request.get_json()
        # 10b. raise Unprocessable Entity
        try:
            for attr in data:
                setattr(q, attr, data.get(attr))
            db.session.add(q)
            db.session.commit()
        except: 
            raise UnprocessableEntity

        return make_response(q.to_dict(), 200)
api.add_resource(One_Actor, '/actors/<int:id>')
#~~~~~~~~~~~~~~~~~~~~~~~~~~END YOU DO~~~~~~~~~~~~~~~~~~~~~~~

#7d. create fallback
@app.errorhandler(NotFound)
def handle_not_found(e):
    return make_response({
        'message': 'data not found'
    }, 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)