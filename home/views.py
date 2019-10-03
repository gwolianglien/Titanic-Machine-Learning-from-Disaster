from flask import Blueprint

home = Blueprint('home', __name__)

@home.route('/')  # Route for current page
def render_home():
    return "Hello, World!"
