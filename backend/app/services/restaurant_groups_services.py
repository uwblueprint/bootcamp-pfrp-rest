from ..models.restaurant_groups import RestaurantGroups
from ..models.restaurant import Restaurant
from ..models import db


'''
while our business logic is really simple so far, it is beneficial to keep it apart from the controller logic.
separation of concerns leads to maintainable code as the application grows, and also makes the code easier to unit test
'''

def get_restaurant_groups():
    # Restaurant is a SQLAlchemy model, we can use convenient methods provided
    # by SQLAlchemy like query.all() to query the data
    return [result.to_dict() for result in Restaurant.query.all()]


def get_restaurant_groups(id):
    # get queries by the primary key, which is id for the Restaurant table
    restaurantGroups = RestaurantGroups.query.get(id)
    if restaurantGroups is None:
        return restaurantGroups
    return restaurantGroups.to_dict()


def create_restaurant_groups(restaurantGroups):
    new_restaurant_groups = RestaurantGroups(**restaurantGroups)
    db.session.add(new_restaurant_groups)
    # remember to commit to actually persist into the database
    db.session.commit()

    return new_restaurant_groups.to_dict()


def update_restaurant_groups(id, restaurant_groups):
    RestaurantGroups.query.filter_by(id=id).update(restaurant_groups)
    updated_restaurant_groups = RestaurantGroups.query.get(id)
    db.session.commit()

    if updated_restaurant_groups is None:
        return updated_restaurant_groups
    return updated_restaurant_groups.to_dict()


def delete_restaurant_groups(id):
    deleted = RestaurantGroups.query.filter_by(id=id).delete()
    db.session.commit()
    
    # deleted is the number of rows deleted
    if deleted == 1:
        return id
    return None
