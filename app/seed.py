#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Pizza, RestaurantPizza, Restaurant

ingredients = [
    "Platformer",
    "Shooter",
    "Fighting",
    "Stealth",
    "Survival",
    "Rhythm",
    "Survival Horror",
    "Metroidvania",
    "Text-Based",
    "Visual Novel",
    "Tile-Matching",
    "Puzzle",
    "Action RPG",
    "MMORPG",
    "Tactical RPG",
    "JRPG",
    "Life Simulator",
    "Vehicle Simulator",
    "Tower Defense",
    "Turn-Based Strategy",
    "Racing",
    "Sports",
    "Party",
    "Trivia",
    "Sandbox"
]

fake = Faker()

with app.app_context():

    Pizza.query.delete()
    RestaurantPizza.query.delete()
    Restaurant.query.delete()

    restaurants = []
    for i in range(20):
        u = Restaurant(name=fake.name(), address=fake.name(),)
        restaurants.append(u)

    db.session.add_all(restaurants)

    pizzas = []
    for i in range(20):
        g = Pizza(
            name=fake.sentence(),
            ingredients=rc(ingredients),
        )
        pizzas.append(g)

    db.session.add_all(pizzas)

    restaurantpizzas = []
    for u in restaurants:
        for i in range(randint(100, 1000)):
            r = RestaurantPizza(
                price=randint(0, 10),
                restaurant=u,
                pizza=rc(pizzas))
            restaurantpizzas.append(r)

    db.session.add_all(restaurantpizzas)

    for g in pizzas:
        r = rc(restaurantpizzas)
        g.restaurantpizza = r
        restaurantpizzas.remove(r)

    db.session.commit()
