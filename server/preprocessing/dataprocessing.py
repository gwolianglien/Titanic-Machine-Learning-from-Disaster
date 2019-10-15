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

test_data = 'test.csv'
train_data = 'train.csv'
test = pd.read_csv(test_data, keep_default_na=False)
train = pd.read_csv(train_data, keep_default_na=False)

train.head(5)


#%%
# Extract only the features that will be used in the model
features = ['Survived', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
df = train[features]
df.head(5)


#%%
# Convert Sex to binary (male: 0, female: 1)
df.loc[df.Sex == 'female', 'Sex'] = 1
df.loc[df.Sex == 'male', 'Sex'] = 0
df.head(5)


#%%
df['Family'] = df['SibSp'] + df['Parch']
df.head(5)


#%%
# Remove SibSp and Parch columns
df.drop('SibSp', axis=1, inplace=True)
df.drop('Parch', axis=1, inplace=True)
df.head(5)


#%%
df = df[(df['Age'] != "")]


#%%
df.to_csv('titanic_model_data.csv', index=False)


