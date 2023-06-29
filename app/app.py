from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Restaurant, Pizza, RestaurantPizza API"

@app.route('/pizzas')
def pizzas():

    pizzas = []
    for pizza in Pizza.query.all():
        pizza_dict = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients,
            
        }
        pizzas.append(pizza_dict)

    response = make_response(
        jsonify(pizzas),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response


# @app.route('/restautantpizzas', methods=['GET', 'POST'])
# def restautantpizzas():

#     if request.method == 'GET':
#         restautantpizzas = []
#         for restautantpizza in RestaurantPizza.query.all():
#             restautantpizza_dict = restautantpizza.to_dict()
#             restautantpizzas.append(restautantpizza_dict)

#         response = make_response(
#             jsonify(restautantpizzas),
#             200
#         )

#         return response

#     elif request.method == 'POST':
#         new_restautantpizza = RestaurantPizza(
#             price=request.form.get("price"),
#              pizza_id=request.form.get(" pizza_id"),
#             restaurant_id=request.form.get("restaurant_id"),
#         )

#         db.session.add(new_restautantpizza)
#         db.session.commit()

#         restautantpizza_dict = new_restautantpizza.to_dict()

#         response = make_response(
#             jsonify(restautantpizza_dict),
#             201
#         )

#         return response

@app.route('/restautantpizzas', methods=['GET', 'POST'])
def restautantpizzas():

    if request.method == 'GET':
        restautantpizzas = []
        for restautantpizza in RestaurantPizza.query.all():
            restautantpizza_dict = restautantpizza.to_dict()
            restautantpizzas.append(restautantpizza_dict)

        response = make_response(
            jsonify(restautantpizzas),
            200
        )

        return response

    elif request.method == 'POST':
        new_restautantpizza = RestaurantPizza(
            price=request.form.get("price"),
            pizza_id=request.form.get("pizza_id"),
            restaurant_id=request.form.get("restaurant_id"),
        )

        db.session.add(new_restautantpizza)
        db.session.commit()

        restautantpizza_dict = new_restautantpizza.to_dict()

        response = make_response(
            jsonify(restautantpizza_dict),
            201
        )

        return response


@app.route('/restaurants')
def get_restaurants():

    restaurants = []
    for restaurant in Restaurant.query.all():
        restaurant_dict = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            
        }
        restaurants.append(restaurant_dict)

    response = make_response(
        jsonify(restaurants),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/restaurants/<int:id>')
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.filter_by(id=id).first()

    restaurant_dict = {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        
    }

    response = make_response(
        jsonify(restaurant_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def delete_restaurant_by_id(id):
    restaurant = Restaurant.query.filter_by(id=id).first()

    if request.method == 'GET':
        restaurant_dict = restaurant.to_dict()

        response = make_response(
            jsonify(restaurant_dict),
            200
        )

        return response

    elif request.method == 'DELETE':
        db.session.delete(restaurant)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Restaurant deleted."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response

if __name__ == '__main__':
    app.run(port=5555)
