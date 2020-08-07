# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 08:53:23 2020

@author: Vaish
"""

# =============================================================================
#   linear regression 
#   
#   target - numeric 
#   future - numeric 
#   function - linear regression 
#   accuracy - r-squared 
#   error - mean squared error 
# =============================================================================
  
# =============================================================================
#   logistic regression 
#   
#   target - binary 
#   feature - any value (char/numeric)
#   function - logistic regression 
#   model validation -  confusion matrix 
#                       accuracy score 
#                       classification report 
# =============================================================================

# =============================================================================
#   logistic Regression 
#   - is used to predict target variable when it is binary 
#   - like predicting win/loss of a team 
#   - predicting selection and no selection of a candidate 
#   - predicting heart attack/ no heart attack of a patient 
#   - logistic regression is in the form of 
#   - logit(P) = weight*X+bias
#   - where P stands for probablity of success
#   - logit(P) = log(P/1-P)
#   - weight - coeffecient 
#   - X - Feature 
#   - bias - constant or intercept 
# =============================================================================
  
# =============================================================================
#   assumption of logistic regression 
#   1. mean not be in linear relation 
#   2. need to havee normal distribution 
#   3. need not have homoscedacity 
#   4. can have multicolinearity 
#   5. need large sample data set (n>500)
# =============================================================================

import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

titanic=pd.read_csv("G:/spyder/Python Part 2 ClassNotes/Class 11B/Titanic.csv")

titanic.shape
titanic.columns
# =============================================================================
#  'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object'
# =============================================================================

# data cleaning 
# drop identification variables 
# find the missinng values for each variables 
# if number of missing values is more than 40%, then drop it 
# numeric missing values replace it by median 
# character missing values drop observation or replace it by mode
# convert character variables into numeric variables.

titanic2=titanic.drop(['PassengerId','Ticket','Name'],axis=1)
titanic2.shape # (891,9)

titanic2.isnull().sum() # let you know the number of missing value 

titanic2.isnull().sum()/len(titanic2) # let you know the percent of missing value in each column 

titanic2.drop(['Cabin'],axis=1,inplace=True) # more than 40% missing value so drop the column
# inplace=True - is used to store the result inn the same location 

import numpy as np 
titanic2=titanic2.replace(np.nan,titanic2.median())

titanic3=titanic2.dropna(axis=0)

titanic3.isnull().sum()
titanic3.shape # 889,8

# converting character variables to dummy variables
# sex and embarked 
titanic3['Sex'].unique()
titanic3['Embarked'].unique()

gender=pd.get_dummies(titanic3['Sex'],drop_first=True)

embark=pd.get_dummies(titanic3['Embarked'],drop_first=True)

titanic3.drop(['Sex','Embarked'],axis=1,inplace=True)
titanic4=pd.concat([titanic3,gender,embark],axis=1)

titanic4.shape # 889,9

X = titanic4.iloc[:,1:]
Y = titanic4.iloc[:,0]

train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.3,random_state=10)

logistic_model=LogisticRegression().fit(train_x,train_y)

pred_y=logistic_model.predict(test_x)

# model validation 

print(confusion_matrix(test_y,pred_y)) # how good the model btw predicted and actual score 
print(accuracy_score(test_y,pred_y)) #0.801 - good fit
print(classification_report(test_y,pred_y)) # precission of 0 and recall of 0 
# F1 score = harmonic mean of precission and recall






























