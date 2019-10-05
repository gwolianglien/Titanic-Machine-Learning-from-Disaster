import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression


def predict(user_input):
    """
    :type user_input: List (Python List, 1-D)
    :rtype: int
    """
    try:
        df = pd.read_csv('../data/titanic_model_data.csv', keep_default_na=False)
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


def check_number_input(input):
    if type(input) == int or type(input == float):
        return True
    return False


def convert_gender(gender):
    if gender == 'Female':
        return 1
    else:
        return 0
