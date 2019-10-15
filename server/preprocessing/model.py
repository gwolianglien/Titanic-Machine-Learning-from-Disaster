# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'data'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd
import numpy as np
import random
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('titanic_model_data.csv', keep_default_na=False)
df.head(5)


#%%
# Linear Model

X = df[['Age', 'Family', 'Fare', 'Sex']]
Y = df[['Survived']]
lin_model = LogisticRegression(solver='lbfgs')
lin_model.fit(X,Y)

test = np.array([25, 3, 25, 0])
test = test.reshape(1,-1)
res = lin_model.predict(test)
res[0]


#%%



