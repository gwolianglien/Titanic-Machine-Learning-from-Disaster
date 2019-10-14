import os
import pickle
import pandas as pd
import numpy as np


def get_model(filepath):
    try:
        loaded_model = pickle.load(open(filepath, 'rb'))
        return loaded_model
    except FileNotFoundError:
        raise Exception('Error loading saved model')


def get_result_string(string):
    if string == "0":
        return "You would not have survived :("
    return "You would have survived! :)"


def set_number_input(num, feature):
    """
    :type input: number (int or float)
    :rtype: Boolean
    """
    try:
        temp = int(num)
        return temp
    except AssertionError:
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
    except AssertionError:
        raise Exception('Error retrieving Averages')  # Temporary - need better method of handling this error


def get_gender(sex):
    """
    :type sex: str
    :rtype: int
    """
    try:
        return 1 if sex.lower() == 'female' else 0
    except AssertionError:
        return 0  # Temporary - need better method of handling this error


# def get_prediction(user):
#     """
#     :type user_input: List (Python List, 1-D)
#     :rtype: int
#     """
#     user = np.array(user).reshape(1,-1)
#     try:
#         df = pd.read_csv('titanic_model_data.csv', keep_default_na=False)
#         model = train(df)
#         prediction = model.predict(user)
#         return str(prediction[0])
#     except:
#         err_msg = "Something went wrong on our end! Try again later!"
#         res = Response(err_msg, status=500)
#         return res
#
#
# def train(df):
#     """
#     :type df: Pandas Dataframe
#     :rtype: Sklearn Linear Model
#     """
#     expected_columns = { 'Age': 0, 'Family': 0, 'Fare': 0, 'Sex': 0, 'Survived': 0 }
#     for col in df:
#         if col in expected_columns:
#             expected_columns[col] += 1
#
#     for col in expected_columns:
#         count = expected_columns[col]
#         if count == 0:
#             raise Exception('Missing {} column in data file'.format(col))
#
#     X = df[['Age', 'Family', 'Fare', 'Sex']]
#     Y = df['Survived']
#     lin_model = LogisticRegression(solver='lbfgs')
#     lin_model.fit(X,Y)
#     return lin_model
