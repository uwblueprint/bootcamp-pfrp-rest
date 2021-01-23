from flask import Blueprint, request
from flask import jsonify

from ..resources.restaurant_resource import RestaurantResource
from ..services import restaurant_service

# this is the controller layer of the application (MVC), it is only responsible for receiving requests and sending responses
# it should be kept lean, all business logic belongs in the service layer

# defines a shared URL prefix for all routes
blueprint = Blueprint('restaurant', __name__, url_prefix='/restaurants')

# defines GET endpoint for retrieving all restaurants
@blueprint.route('/', methods=['GET'], strict_slashes=False)
def get_restaurants():
    # restaurant_service does the actually fetching of restaurants
    result = restaurant_service.get_restaurants()
    # HTTP status code 200 means OK
    return jsonify(result), 200


# defines GET endpoint for retrieving a single restaurant based on a provided id
@blueprint.route('/<int:id>', methods=['GET'], strict_slashes=False)
def get_restaurant(id):
    result = restaurant_service.get_restaurant(id)
    if result is None:
        error = {'error': 'restaurant not found'}
        # HTTP status code 404 means Not Found
        return jsonify(error), 404

    # HTTP status code 200 means OK
    return jsonify(result), 200


# define POST endpoint for creating a restaurant
@blueprint.route('/', methods=['POST'], strict_slashes=False)
def create_restaurant():
    try:
        # create a RestaurantResource object instead of using the raw request body
        # data validators and transformations are applied when constructing the resource,
        # this allows downstream code to make safe assumptions about the data
        body = RestaurantResource(**request.json)
    except Exception as error:
        error = {'error': str(error)}
        # HTTP status code 400 means Bad Request
        return jsonify(error), 400
    
    # HTTP status code 201 means Created
    return jsonify(restaurant_service.create_restaurant(body.__dict__)), 201


# defines PUT endpoint for updating the restaurant with the provided id
@blueprint.route('/<int:id>', methods=['PUT'], strict_slashes=False)
def update_restaurant(id):
    try:
        body = RestaurantResource(**request.json)
    except Exception as error:
        error = {'error': str(error)}
        return jsonify(error), 400
    
    result = restaurant_service.update_restaurant(id, body.__dict__)

    if result is None:
        error = {'error': 'restaurant not found'}
        return jsonify(error), 404
    
    return jsonify(result), 200


# defines DELETE endpoint for deleting the restaurant with the provided id
@blueprint.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_restaurant(id):
    result = restaurant_service.delete_restaurant(id)

    if result is None:
        error = {'error': 'restaurant not found'}
        return jsonify(error), 404
    
    return jsonify(result), 200
