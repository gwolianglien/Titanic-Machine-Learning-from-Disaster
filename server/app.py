from flask import Flask
from api.titanic import titanic
from api.test import test

def create_app(config_file):
    # Create Flask app object
    app = Flask(__name__)  

    # Store config file
    app.config.from_pyfile(config_file)

    # Import routes
    app.register_blueprint(titanic, url_prefix='/titanic')
    app.register_blueprint(test, url_prefix='/test')
    return app


if __name__ == '__main__':
    app = create_app('config.py')
    app.run()  # .run() activates the application
