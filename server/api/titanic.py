from flask import Blueprint, request, Response
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

titanic = Blueprint('titanic', __name__)

@titanic.route('/', methods=['GET'])  # Temporary
def titanic_test_route():
    return "Welcome to the Titanic Game!"


@titanic.route('/', methods=['POST'])  # Route for current page
def predict_user_results():
    """
    :rtype: int
    """

    content = request.json
    age = content['age']
    family = content['family']
    fare = content['fare']
    sex = content['sex']

    age = set_number_input(age, 'Age')
    family = set_number_input(family, 'Family')
    fare = set_number_input(fare, 'Fare')
    sex = convert_gender(sex)    
    user_input = [age, family, fare, sex]

    result = get_prediction(user_input)
    result = get_result_string(result)
    res = Response(result, status=200)
    return res


def get_prediction(user):
    """
    :type user_input: List (Python List, 1-D)
    :rtype: int
    """
    user = np.array(user).reshape(1,-1)
    try:
        df = pd.read_csv('titanic_model_data.csv', keep_default_na=False)
        model = train(df)
        prediction = model.predict(user)
        return str(prediction[0])
    except:
        err_msg = "Something went wrong on our end! Try again later!"
        res = Response(err_msg, status=500)
        return res


def train(df):
    """
    :type df: Pandas Dataframe
    :rtype: Sklearn Linear Model
    """
    expected_columns = { 'Age': 0, 'Family': 0, 'Fare': 0, 'Sex': 0, 'Survived': 0 }
    for col in df:
        if col in expected_columns:
            expected_columns[col] += 1
    
    for col in expected_columns:
        count = expected_columns[col]
        if count == 0:
            raise Exception('Missing {} column in data file'.format(col))

    X = df[['Age', 'Family', 'Fare', 'Sex']]
    Y = df['Survived']
    lin_model = LogisticRegression(solver='lbfgs')
    lin_model.fit(X,Y)
    return lin_model


def get_result_string(string):
    if string == "0":
        return "You would not have survived :("
    return "You would have survived!"


def set_number_input(num, feature):
    """
    :type input: number (int or float)
    :rtype: Boolean
    """
    try:
        temp = int(num)
        return temp
    except:
        return get_average(feature)


def get_average(feature):
    """
    :type feature: str
    :rtype: float
    """
    try:
        df = pd.read_csv('titanic_model_data.csv', keep_default_na=False)
        df = np.array(list(df[feature]))
        return df.mean()
    except:
        return 0  # Temporary - need better method of handling this error


def convert_gender(sex):
    """
    :type sex: str
    :rtype: int
    """
    return 1 if sex.lower() == 'female' else 0