from flask import Blueprint, request
from flask import jsonify

from ..resources.restaurant_groups_resource import RestaurantGroupsResource
from ..services import restaurant_groups_service

# this is the controller layer of the application (MVC), it is only responsible for receiving requests and sending responses
# it should be kept lean, all business logic belongs in the service layer

# defines a shared URL prefix for all routes
# blueprint = Blueprint('restaurant_groups', __name__, url_prefix='/restaurant_groups')
blueprint = Blueprint('restaurant_groups', __name__)


# defines GET endpoint for retrieving all restaurants
@blueprint.route('/', methods=['GET'], strict_slashes=False)
def get_restaurant_groups():
    print("hello")
    # restaurant_service does the actually fetching of restaurants
    result = restaurant_groups_service.get_restaurant_groups()
    # HTTP status code 200 means OK
    return jsonify(result), 200


# defines GET endpoint for retrieving a single restaurant based on a provided id
@blueprint.route('/<int:id>', methods=['GET'], strict_slashes=False)
def get_restaurant_groups(id):
    result = restaurant_groups_service.get_restaurant_groups(id)
    if result is None:
        error = {'error': 'restaurant group not found'}
        # HTTP status code 404 means Not Found
        return jsonify(error), 404

    # HTTP status code 200 means OK
    return jsonify(result), 200


# define POST endpoint for creating a restaurant
@blueprint.route('/', methods=['POST'], strict_slashes=False)
def create_restaurant_groups():
    try:
        # create a RestaurantResource object instead of using the raw request body
        # data validators and transformations are applied when constructing the resource,
        # this allows downstream code to make safe assumptions about the data
        body = RestaurantGroupsResource(**request.json)
    except Exception as error:
        error = {'error': str(error)}
        # HTTP status code 400 means Bad Request
        return jsonify(error), 400
    
    # HTTP status code 201 means Created
    return jsonify(restaurant_groups_service.create_restaurant_groups(body.__dict__)), 201


# defines PUT endpoint for updating the restaurant with the provided id
@blueprint.route('/<int:id>', methods=['PUT'], strict_slashes=False)
def update_restaurant_groups(id):
    try:
        body = RestaurantGroupsResource(**request.json)
    except Exception as error:
        error = {'error': str(error)}
        return jsonify(error), 400
    
    result = restaurant_groups_service.update_restaurant_groups(id, body.__dict__)

    if result is None:
        error = {'error': 'restaurant group not found'}
        return jsonify(error), 404
    
    return jsonify(result), 200


# defines DELETE endpoint for deleting the restaurant with the provided id
@blueprint.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_restaurant_groups(id):
    result = restaurant_groups_service.delete_restaurant(id)

    if result is None:
        error = {'error': 'restaurant group not found'}
        return jsonify(error), 404
    
    return jsonify(result), 200
