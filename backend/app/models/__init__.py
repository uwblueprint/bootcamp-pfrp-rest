from flask_sqlalchemy import SQLAlchemy

from .restaurant_seed_data import restaurant_seed_data


# instantiate a SQLAlchemy instance, it provides an abstraction over our PostgreSQL database
db = SQLAlchemy()
# set erase_db_and_sync = True if you want to seed the database or if you need to change the schema
# be careful since it will drop all existing tables!
#
# typically we would use migrations to modify the DB schema, especially for production apps
# migrations are safer and offer more fine-grained controls. However, for simplicity, we won't use migrations for bootcamp
erase_db_and_sync = True

def init_app(app):
    # look at restaurant.py for the model (and table) definition
    from .restaurant import Restaurant

    app.app_context().push()
    # uses the SQLALCHEMY_DATABASE_URI we set earlier to connect to the DB
    db.init_app(app)

    if erase_db_and_sync:
        # drop tables
        db.reflect()
        db.drop_all()

        # recreate tables
        db.create_all()

        # add seed data
        for restaurant in restaurant_seed_data:
            db.session.add(Restaurant(**restaurant))
        db.session.commit()
