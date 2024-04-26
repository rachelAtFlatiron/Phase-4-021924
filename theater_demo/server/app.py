#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request, abort
from flask_migrate import Migrate 
from models import db, Production, Role, Actor
# 2a. import Api, Resource
from flask_restful import Api, Resource


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

migrate = Migrate(app, db)

# 2b. create Api instance
# hooked up flask app to flask_restful Api
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
def all_productions():
    if(request.method=="GET"):
        q = Production.query.all()
        prod_list = [p.to_dict() for p in q]
        res = make_response(jsonify(prod_list), 200)
        return res 
    
    if(request.method=="POST"):
        data = request.get_json()
        prod = Production(title=data.get('title'), genre=data.get('genre'), length=data.get('length'), year=data.get('year'), image=data.get('image'), language=data.get('language'), director=data.get('director'), description=data.get('description'), composer=data.get('composer') )
        db.session.add(prod)
        db.session.commit()

        dict = prod.to_dict()
        return make_response(jsonify(dict), 201)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/productions/<int:id>', methods=["GET", "DELETE"])
def get_one_production(id):
    if(request.method == 'GET'):
        q = Production.query.filter_by(id=id).first()
        prod_dict = q.to_dict()
        res = make_response(jsonify(prod_dict), 200)
        return res

    if(request.method == "DELETE"):
        q = Production.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3a. create resource for roles
class Roles(Resource):
    def get(self):
        q = Role.query.all()
        q_dict = [r.to_dict(rules=('-production', '-actor')) for r in q]
        return make_response(q_dict)

    def post(self):
        data = request.get_json()
        role = Role(
            role_name=data.get('role_name'),
            production_id=data.get('production_id'),
            actor_id=data.get('actor_id')
        )
        db.session.add(role)
        db.session.commit()
        return make_response(role.to_dict(), 201)
    
    # 3b. create view method for all roles
    # 3c. add rules to .to_dict()

    
    #4a. create POST view method

    
# 3d. create api endpoint for Roles 
api.add_resource(Roles, '/roles')

# 5a. create resource for SHOW and DELETE  
class One_Role(Resource):
    def get(self, id):
        q = Role.query.filter_by(id=id).first()
        return make_response(q.to_dict())

    def delete(self, id):
        q = Role.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)

    def patch(self, id):
        q = Role.query.filter_by(id=id).first()
        #there are a number of formats you can pass data in
        #we will be using JSON
        #since we have headers content-type: application/json
        data = request.get_json()  

        for attr in data:
            setattr(q, attr, data.get(attr))

        db.session.add(q)
        db.session.commit()

        return make_response(q.to_dict())

    # 5b. create SHOW view method

    # 5c. create DELETE view method

    # 6. Create a PATCH view method
        # 6a. get matching query
        # 6b. iterate over attributes from request
        # 6c. update available attributes from request

        # 6d. add, commit to database

    
# 5d. create an API endpoint for One_Role
api.add_resource(One_Role, '/roles/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)