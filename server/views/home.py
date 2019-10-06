from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')  # Route for current page
def render_home():
    return render_template('home.html')
