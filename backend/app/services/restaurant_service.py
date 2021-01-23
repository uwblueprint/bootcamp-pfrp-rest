from ..models.restaurant import Restaurant
from ..models import db


'''
while our business logic is really simple so far, it is beneficial to keep it apart from the controller logic.
separation of concerns leads to maintainable code as the application grows, and also makes the code easier to unit test
'''

def get_restaurants():
    # Restaurant is a SQLAlchemy model, we can use convenient methods provided
    # by SQLAlchemy like query.all() to query the data
    return [result.to_dict() for result in Restaurant.query.all()]


def get_restaurant(id):
    # get queries by the primary key, which is id for the Restaurant table
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return restaurant
    return restaurant.to_dict()


def create_restaurant(restaurant):
    new_restaurant = Restaurant(**restaurant)
    db.session.add(new_restaurant)
    # remember to commit to actually persist into the database
    db.session.commit()

    return new_restaurant.to_dict()


def update_restaurant(id, restaurant):
    Restaurant.query.filter_by(id=id).update(restaurant)
    updated_restaurant = Restaurant.query.get(id)
    db.session.commit()

    if updated_restaurant is None:
        return updated_restaurant
    return updated_restaurant.to_dict()


def delete_restaurant(id):
    deleted = Restaurant.query.filter_by(id=id).delete()
    db.session.commit()
    
    # deleted is the number of rows deleted
    if deleted == 1:
        return id
    return None
