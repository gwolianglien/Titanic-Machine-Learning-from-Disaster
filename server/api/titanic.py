from flask import Blueprint, request, Response
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression


from actions.model import get_model, set_number_input, get_gender, get_result_string

titanic = Blueprint('titanic', __name__)

@titanic.route('/', methods=['GET'])  # Temporary
def titanic_test_route():
    return "Welcome to the Titanic Game!"


@titanic.route('/', methods=['POST'])  # Route for current page
def predict_user_results():
    """
    :rtype: int
    """

    content = request.get_json()

    age = content.get("age")
    family = content.get("family")
    fare = content.get("fare")
    sex = content.get("sex")

    age = set_number_input(age, 'Age')
    family = set_number_input(family, 'Family')
    fare = set_number_input(fare, 'Fare')
    sex = get_gender(sex)
    user_input = [age, family, fare, sex]

    model = get_model()  # load model with pickle

    try:
        user = np.array(user_input).reshape(1, -1)
        prediction = model.predict(user)
        result = get_result_string(str(prediction[0]))
        res = Response(result, status=200)
        return res
    except:
        res = Response('Server Error', status=500)
        return res
