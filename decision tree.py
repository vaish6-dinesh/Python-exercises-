# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:03:04 2020

@author: Vaish
"""

# =============================================================================
#   Decision tree 
#   descision tree is used to predict the target variables using a tree structure 
#   model 
#   tree model will be build using two methods 
#   1. CART MODEL gini index (gini = sum(p^2,q^2))
#   2. ID3 MODEL entropy and information gain 
#           entropy - sum(-p*log2p, -q*log2q)
#           information gain - entropy of target - enttropy of feature 
# =============================================================================
          
#  Select the root node variable will depend upon highest gini value 
#  or highest information gain values.
  
          
import pandas as pd 
balance=pd.read_csv('G:/spyder/Python Part 2 ClassNotes/Class 12/balance_scale.csv')
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score 
from sklearn.metrics import classification_report
balance=pd.read_csv('G:/spyder/Python Part 2 ClassNotes/Class 12/balance_scale.csv',header=None)

balance.shape
balance.columns

balance.isnull().sum()

X = balance.iloc[:,1:]
Y = balance.iloc[:,0]

train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.3,
                                              random_state=10)


# gini method
model_gini=DecisionTreeClassifier(criterion="gini").fit(train_x,train_y)

pred_y = model_gini.predict(test_x)

print("gini results")
print(confusion_matrix(test_y,pred_y))
print(accuracy_score(test_y,pred_y))  # 0.75 and above so it is good fit
print(classification_report(test_y,pred_y))

#entropy method

model_entropy=DecisionTreeClassifier(criterion="entropy").fit(train_x,train_y)

pred_y = model_entropy.predict(test_x)

print("entropy results")
print(confusion_matrix(test_y,pred_y))
print(accuracy_score(test_y,pred_y))  # 0.75 and above so it is good fit
print(classification_report(test_y,pred_y))

# case study 
# predict class value from case 2 data.xlsx sheet2
# build the decision tree

import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score 
from sklearn.metrics import classification_report
data=pd.read_excel('G:/spyder/Python Part 2 ClassNotes/Class 12/Case Study/Case 2/Data.xlsx',sheet_names="Sheet2")

data.shape
data.columns


data.isnull().sum()

X = data.iloc[:,-1:]
Y = data.iloc[:,-1]

train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.3,
                                              random_state=10)


# gini method
model_gini=DecisionTreeClassifier(criterion="gini").fit(train_x,train_y)

pred_y = model_gini.predict(test_x)

print("gini results")
print(confusion_matrix(test_y,pred_y))
print(accuracy_score(test_y,pred_y))  # 1.0 is the best fit
print(classification_report(test_y,pred_y))

# when you are getting the model as 1.0 then the model is over fit 
import seaborn as sns
sns.heatmap(data.corr())

# test 
#chi square 
#significance test ttest anova
#regression
#logistic regression

 















































9