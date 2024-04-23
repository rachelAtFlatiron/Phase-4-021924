# handle creating the api and connecting the database 
# and enabling alembic/migrations

# ✅ 1. Navigate to `models.py`

# ✅ 2a. Set Up Imports
from flask import Flask, make_response
from flask_migrate import Migrate 
from models import db, Production
from sqlalchemy import desc
# Flask (API) <- ORM (SQLAlchemy) <- Migrate (takes ORM python and converts to SQL/creates database)

# ✅ 2b. Create instance of Flask
app = Flask(__name__)
# ✅ 2c. Configure the flask app to connect to a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
# ✅ 2d. Enable Flask-Migrate's Alembic by using `Migrate`
migrate = Migrate(app, db)
# ✅ 2e. Connect the database to the app
db.init_app(app)

# ✅ 3. Migrate the Production model using Flask-Migrate's Alembic

# > flask db init: create our templated folder structure and files
# > flask db migrate --autogenerate -m 'Create tables productions': autogenerate a migration file which has instructions as to how to populate the database
# it also creates an empty .db file 
# flask db upgrade head : applies (commits) migration file to app.db (thus ACTUALLY changing the .db file)

# ✅ 4. Navigate to `seed.rb`

# ✅ 6. Create a path to retrieve the first 5 longest movies
# ✅ 6a. Import jsonify, make_response
# ✅ 6b. Use the `route` decorator
# ✅ 6c. Query for longest movie
# ✅ 6d. Jsonify and return the response
@app.route('/longest-movies')
def longest_movies():
    q = Production.query.order_by(desc('length')).limit(5)
    prod_list = [p.to_dict(only=('title', 'length')) for p in q]
    return make_response(prod_list)


# ✅ 7. Create a dynamic route
# ✅ 7a. Use the route decorator
# ✅ 7b. Create productions() to filter through db

# ✅ 7c. Return result as JSON

# ✅ 8. Create a dynamic route `/productions/<int:id>` that searches for all matching records
@app.route('/productions/<int:prod_id>')
def one_production(prod_id):
    # .query only returns class instances
    # .query is Flask-SQLAlchemy
    # our Flask-SQLAlchemy is class based
    # so we have to convert things to something that is acceptable for a response
    # i.e. tuple, list, dictionary, etc.
    q = Production.query.filter_by(id=prod_id).first()
    # .to_dict() (via SerializerMixin - see models.py) will convert the SQLAlchemy instance into a dictionary 
    return make_response(q.to_dict(), 200)

# ✅ 9. Create a route `/all-productions` to see all productions
@app.route('/productions')
def all_productions():
    q = Production.query.all()
    # SERIALIZER RULE EXPECTS TUPLE 
    # IF YOU ONLY HAVE ONE THING IN YOUR TUPLE
    # DON'T FORGET THE TRAILING COMMA
    prod_list = [p.to_dict(only=('title', )) for p in q]
    return make_response(prod_list, 200)
# ✅ 9a. use SerializerMixin's .to_dict() for responses here and everywhere


# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

if __name__ == '__main__':
    app.run(port=5555, debug=True)