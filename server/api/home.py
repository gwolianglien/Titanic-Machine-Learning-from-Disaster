from flask import Blueprint, render_template, request

home = Blueprint('home', __name__)

@home.route('/')  # Route for current page
def render_home():
    return render_template('home.html')


@home.route('/run', methods=['POST'])
def get_user_survivability():

    sex = request.form.get('sex')
    age = request.form.get('age')
    fare = request.form.get('fare')
    family = request.form.get('family')

    if check_number_input(age) is False:
        age = 18  # change this to average age if none is found
    if check_number_input(fare) is False:
        fare = 20  # same condition as age
    if check_number_input(family) is False:
        family = 2  # same condition as age
    sex = convert_gender(sex)
    return [age, family, fare, sex]


def check_number_input(input):
    if type(input) == int or type(input == float):
        return True
    return False


def convert_gender(gender):
    if gender == 'Female':
        return 1
    else:
        return 0
