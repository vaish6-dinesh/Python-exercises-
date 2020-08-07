# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:26:50 2020

@author: Vaish
"""

bank=pd.read_csv('G:/spyder/Python Part 2 ClassNotes/Class 11B/Logistic regression/Case1/bank.csv')

bank.shape
bank.columns

import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

bank.isnull().sum()
bank.isnull().sum()/len(bank)

titanic3['Sex'].unique()
titanic3['Embarked'].unique()

gender=pd.get_dummies(titanic3['housing'],drop_first=True)

martialstatus=pd.get_dummies(bank['maritial'],drop_first=True)

titanic3.drop(['Sex','Embarked'],axis=1,inplace=True)
titanic4=pd.concat([titanic3,gender,embark],axis=1)
