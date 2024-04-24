from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()
class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

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

    roles = db.relationship('Role', back_populates='production')
    actors = association_proxy('roles', 'actor')


    serialize_rules = ('-roles.production', '-created_at', '-updated_at',  '-image', '-director', '-composer')
    '''
    productionA {
        id, 
        title,
        roles: [
            productionA {
                roles: [
                    productionA: {
                        roles...
                    }
                ]
            }
        ]
    }
    '''
    def __repr__(self):
        return f'<Production id={self.id} title={self.title} />'


# ✅ 1. Create a Role model
class Role(db.Model, SerializerMixin):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    role_name = db.Column(db.String)

    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    # ✅ 1a. Create a one-to-many relationship between `Role` and `Production`
    production = db.relationship('Production', back_populates='roles')

    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))
    actor = db.relationship('Actor', back_populates='roles')
    # ✅ 1b. Fetch the route `/productions` to see all the roles associated with each production
    # ✅ 1c. Create a `/roles` route to see the other side of the one-to-many relationship
    serialize_rules = ('-updated_at', '-created_at', '-production.roles', '-actor.roles')

    def __repr__(self):
        return f'<Role id={self.id} name={self.role_name} />'

# ✅ 2. Create an `Actor` model
class Actor(db.Model, SerializerMixin):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    name = db.Column(db.String)
    image = db.Column(db.String)
    age = db.Column(db.Integer)
    country = db.Column(db.String)

    roles = db.relationship('Role', back_populates="actor")
    productions = association_proxy('roles', 'production')
    
    serialize_rules = ('-created_at', '-updated_at', '-roles.actor', '-image', '-roles.production')

    def __repr__(self):
        return f'<Actor id={self.id} name={self.name} />'
    
    # ✅ 2a. Create a one-to-many relationship between `Role` and `Actor`
    # ✅ 2b. Fetch the route `/roles` to see all the roles associated with each actor
    # ✅ 2c. Create an `/actors` route to see the other side of the one-to-many relationship
    # ✅ 3. Create many-to-many relationship between `Production` and `Actor` using `association_proxy`
    # ✅ 3a. Use `SerializerMixin` to prevent max recursion
    # ✅ 3b. Create routes to access all actors and all productions


'''
actor -> roles <- production

actor: roles
roles: actor, production
production: roles
'''