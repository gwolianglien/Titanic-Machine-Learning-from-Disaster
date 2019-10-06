from flask import Flask
# from views.home import home as home_view
# from api.titanic import titanic
from api.test import test

def create_app(config_file):
    # Create Flask app object
    app = Flask(__name__)  

    # Sort of like a default JSON file to store constants and keys
    app.config.from_pyfile(config_file)

    # Very much like ExpressJS where you import and require a route
    # app.register_blueprint(home_view)
    # app.register_blueprint(titanic, url_prefix='/predict')
    app.register_blueprint(test, url_prefix='/test/')
    return app


if __name__ == '__main__':
    app = create_app('config.py')
    app.run()  # .run() activates the application
