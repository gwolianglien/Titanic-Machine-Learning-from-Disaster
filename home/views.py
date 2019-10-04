from flask import Blueprint, render_template, request

home = Blueprint('home', __name__)

@home.route('/')  # Route for current page
def render_home():
    return render_template('home.html')


@home.route('/', methods=['POST'])
def get_user_inputs():
    gender = request.form.get('gender')
    age = request.form.get('age')
    ticket = request.form.get('ticket')
    family = request.form.get('family')

    if check_number_input(age) is False or check_number_input(ticket) is False or check_number_input(family) is False:
        raise Exception('Input Error')

    gender = convert_gender(gender)


def check_number_input(input):
    if type(input) != int and type(input) != float:
        return False
    return True


def convert_gender(gender):
    if gender == 'Male':
        return 0
    if gender == 'Female':
        return 1
    raise Exception('Unexpected gender type')