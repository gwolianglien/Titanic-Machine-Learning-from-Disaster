from flask import Blueprint, request
from ast import literal_eval
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

titanic = Blueprint('titanic', __name__)

@titanic.route('/', methods=['POST'])  # Route for current page
def predict_user_results(obj):
    """
    :type obj: Stringified JSON Object
    :rtype: int
    """

    parsed = literal_eval(obj)
    sex = parsed['sex']
    age = parsed['age']
    fare = parsed['fare']
    family = parsed['family']

    if check_number_input(age) is False:
        age = get_average('Age')
    if check_number_input(fare) is False:
        fare = get_average('Fare')
    if check_number_input(family) is False:
        family = get_average('Family')
    sex = convert_gender(sex)

    user_input = [age, family, fare, sex]
    res = predict(user_input)
    return res[0]


def predict(user_input):
    """
    :type user_input: List (Python List, 1-D)
    :rtype: int
    """
    try:
        df = pd.read_csv('../../data/titanic_model_data.csv', keep_default_na=False)
        model = train(df)
        user_input = user_input.reshape(1,-1)
        res = model.predict(user_input)
        return res[0]
    except:
        return "Something went wrong on our end! Try again later!"


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
    Y = df[['Survived']]
    lin_model = LogisticRegression(solver='lbfgs')
    lin_model.fit(X,Y)
    return lin_model


def get_average(feature='Age'):
    """
    :type feature: str
    :rtype: float
    """
    df = pd.read_csv('../../data/titanic_model_data.csv', keep_default_na=False)
    df = np.array(list(df[feature]))
    return df.mean()


def check_number_input(input):
    """
    :type input: number (int or float)
    :rtype: Boolean
    """
    return True if type(input) == int or type(input == float) else False


def convert_gender(sex):
    """
    :type sex: str
    :rtype: int
    """
    return 1 if sex.lower() == 'female' else 0
