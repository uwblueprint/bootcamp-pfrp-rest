import os
from dotenv import load_dotenv

# note: VS Code's Python extension might falsely report an unresolved import, you can ignore it
from app import create_app


# the entrypoint to our app
if __name__ == '__main__':
    # load environment variables from .env so that we can access them with os.getenv()
    load_dotenv()

    # create our application, which is Flask web server
    # Flask is a Python framework, it provides useful methods for building a web backend
    config_name = os.getenv('FLASK_CONFIG') or 'development'
    # go to app/__init__.py to see the create_app definition
    app = create_app(config_name)

    # run the app, it listens on port 8080
    app.run(host='0.0.0.0', port=8080)
