import os
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression


def main():
    try:
        df = pd.read_csv('../data/titanic_model_data.csv', keep_default_na=False)
        linear_model = train(df)
        filename = 'finalized_model.sav'

        path = '../api/models/'
        if not os.path.exists(path):
            os.makedirs(path)

        pickle.dump(linear_model, open(os.path.join(path, filename), 'wb'))
    except:
        raise Exception('Error training model')


def train(df: object) -> object:
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


if __name__ == '__main__':
    main()
