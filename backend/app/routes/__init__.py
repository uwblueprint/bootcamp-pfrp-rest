def init_app(app):
    from . import restaurant_routes

    # see restaurant_routes.py for route definitions
    app.register_blueprint(restaurant_routes.blueprint)
