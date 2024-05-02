#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request, abort, session
from flask_migrate import Migrate 
from models import db, Production, Role, Actor, User
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound, UnprocessableEntity, Unauthorized

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

# 2c. create secret key
app.secret_key = b"\xa5,\x9cy\x00\x82\x0b\x1b\x11Q\xe9.z'\x07\xf7"

migrate = Migrate(app, db)

api = Api(app)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/longest-movies')
def get_longest_movies():
    prods = Production.query.order_by(Production.length.desc()).limit(5)
    prods_list = [prod.to_dict() for prod in prods]
    return make_response(prods_list, 200)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ✅ 1a. put some cookies in inspector of browser
# ✅ 1a. create a GET route for dark-mode
    # ✅ 1c. import ipdb; ipdb.set_trace()
    # ✅ 1d. send a response with cookies info
@app.route('/dark-mode')
def mode():
    #import ipdb; ipdb.set_trace()
    return make_response({
        "cookies": request.cookies["mode"]
    })
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ✅ 2a. In `app.py` create a new user
class Users(Resource):
    def post(self):
        data = request.get_json()
        user = User(name=data.get('name'), username=data.get('username'))
        db.session.add(user)
        db.session.commit()

        # ✅ 2b. import session from flask
        # ✅ 2c. generate secret key to hash session
        # ✅ 2d. save the user_id to session hash
        session['user_id'] = user.id 
        return make_response(user.to_dict(), 201)
        
# ✅ 2e. add resource to route `/users`
api.add_resource(Users, '/users')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ✅ 5a. create /logout route and set session['user_id'] to None
@app.route('/logout', methods=["GET"])
def logout():
    # ✅ 5b. return empty response
    session['user_id'] = None 
    #import ipdb; ipdb.set_trace()
    return make_response({}, 200)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ✅ 8a. create route `/authenticate-session`
@app.route('/authenticate-session', methods=["GET"])
def authorize():
    # ✅ 8b. query for user by `user_id` stored in `session`
    cookie_id = session.get('user_id')
    user = User.query.filter_by(id=cookie_id).first()
    # ✅ 8c. if user exists, send user info as response, otherwise `abort` with `401 Unauthorized`
    if user: 
        return make_response(user.to_dict(), 200)
    else:
        return ({'message': 'failed to authenticate'}, 401)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ✅ 10a. create a /login resource with a method
class Login(Resource):
    def post(self):
        # ✅ 10b. get username from request
        data = request.get_json()
        user = User.query.filter_by(username=data.get('username')).first()
        # ✅ 10c. if user exists, save id to session and return user
        # ✅ 10d. if user does not exist, raise an error
        if (user):
            session['user_id'] = user.id 
            return make_response(user.to_dict(), 200)
        else: 
            return ({'message': 'failed to login'}, 401)
        
api.add_resource(Login, '/login')            

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/productions', methods=["GET", "POST"])
def Productions():
    if(request.method=="GET"):
        q = Production.query.all()
        if not q:
            raise NotFound
        prod_list = [p.to_dict() for p in q]
        res = make_response(jsonify(prod_list), 200)
        return res 
    
    if(request.method=="POST"):
        data = request.get_json()
        try:
            prod = Production(title=data.get('title'), genre=data.get('genre'), length=data.get('length'), year=data.get('year'), image=data.get('image'), language=data.get('language'), director=data.get('director'), description=data.get('description'), composer=data.get('composer') )
            db.session.add(prod)
            db.session.commit()
        except Exception:
            raise UnprocessableEntity('no')

        dict = prod.to_dict()
        return make_response(jsonify(dict), 201)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/productions/<int:id>', methods=["GET", "DELETE"])
def One_Production(id):
    if(request.method == 'GET'):
        q = Production.query.filter_by(id=id).first()
        if not q:
            raise NotFound
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
        if not q:
            abort(404, "The role was not found")
        role_dict = [r.to_dict(only=('id', 'role_name', 'actor.name', 'production.title')) for r in q]
        return make_response(role_dict, 200)
    
    def post(self):
        data = request.get_json()
        try:
            role = Role(role_name=data.get('role_name'), production_id=data.get('production_id'))
            db.session.add(role)
            db.session.commit()
        except Exception:
            raise UnprocessableEntity('no')

        return make_response(role.to_dict(), 201)
    
api.add_resource(Roles, '/roles', '/test')

class One_Role(Resource):

    def get(self, id):
        q = Role.query.filter_by(id=id).first()
        if not q:
            abort(404, "The role was not found")
        return make_response(q.to_dict(), 200)
    def delete(self, id):
        q = Role.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)
    def patch(self, id):
        q = Role.query.filter_by(id=id).first()
        data = request.get_json()
        try:
            for attr in data:
                setattr(q, attr, data.get(attr))
            db.session.add(q)
            db.session.commit()
        except Exception:
            raise UnprocessableEntity('no')
        return make_response(q.to_dict(), 200)
    
api.add_resource(One_Role, '/roles/<int:id>')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Actors(Resource):
    def get(self):
        q = Actor.query.all()
        if not q:
            abort(404, "The Actor was not found")
        actor_dict = [a.to_dict() for a in q]
        return make_response(actor_dict, 200)
    
    def post(self):
        data = request.get_json()
        try:
            actor = Actor(name=data.get('name'), image=data.get('image'), age=data.get('age'), country=data.get('country'))
            db.session.add(actor)
            db.session.commit()
        except Exception:
            raise UnprocessableEntity('no')

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
        try:
            for attr in data:
                setattr(q, attr, data.get(attr))
            db.session.add(q)
            db.session.commit()
        except Exception: 
            raise UnprocessableEntity('no')
        return make_response(q.to_dict(), 200)
api.add_resource(One_Actor, '/actors/<int:id>')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "Not Found: Sorry the resource you are looking for does not exist",
        404
    )
    return response

# @app.before_request
# def before_request():
#     import ipdb; ipdb.set_trace()

if __name__ == '__main__':
    app.run(port=5555, debug=True)