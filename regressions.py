# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:22:36 2020

@author: Vaish
"""

# =============================================================================
#   Regrressions 
#   regression is used to predict the targeted variables (dependent variables) using
#   given feature variables (independent variables)
#   target - Y 
#   feature - X
#   predicting sales using discount given.
#   X = discounts , Y = sales 
# =============================================================================
  
# =============================================================================
#   Difference between prediction and forecast 
#   forecast sales for next week or next month 
#   predict sales for 10% discount 
# =============================================================================
  
# =============================================================================
#   we need to derive an equation in order to predict Y 
#   equation will be in the form of 
#   Y = W*X+ b 
#   where W is weight(coefficient)
#   b is bias (intercept)
# =============================================================================
  
# =============================================================================
#   There is some assumption which we have to accept before going to regression 
#   1. linear relationship between X and Y 
#   2. X and Y must be multivariate and normally distributed 
#   3. Residual (actual - predicted) value must be contant all point of 
#   predicted (same variance - HOMOSCEDASCITY)
#   4. in case of multiple features, there should not be any coorelation between 
#   them (NO MULTICOLLINEARITY)
#   5. Target values must be independent from each other . (NO AUTOCORRELATION)
# =============================================================================

import pandas as pd 
from sklearn import datasets

# from sklearn. import train_test_split

# Regression Analysis 

import pandas as pd 
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error # to cal error value

boston = datasets.load_boston()
boston.DESCR # desciption of the datasets
# X = 13, Y = MEDV, n = 506 

X = pd.DataFrame(boston.data,columns=boston.feature_names)
Y = pd.DataFrame(boston.target,columns=['MEDV'])

X.isnull().sum()
Y.isnull().sum()

# split data into test and train
# train = 70% and test = 30%


train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.3,
                                               random_state=11)

reg_model=LinearRegression().fit(train_x,train_y)

pred_y = reg_model.predict(test_x)

print(mean_squared_error(test_y,pred_y))

# 24.56 mean squared value - average error in predicting 
# boston house price using derived equation 

print(reg_model.score(train_x,train_y))
# R squared = 0.7518 - percentage variation in targeted variables
# explained by derived equation. Higher value is more preffered 
# R squared >= 0.85 - best fit 
# R squared >= 0.7 - good fit 
# R squared < 0.5 - poor fit 


# Assignment 
#  extract the data 
# bulid the regression model 
# target cost 

locs = 'G:/spyder/Python Part 2 ClassNotes/class 11/Assignment/'

auction = pd.read_sas(locs + "auction.sas7bdat")

auction.shape
auction.columns
X = auction.iloc[:,1:5]
Y = auction.iloc[:,5]

train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.3,
                                               random_state=10)


reg_model=LinearRegression().fit(train_x,train_y)



print(mean_squared_error(test_y,pred_y))

# 0.94 means best fit model 
# coeffcient 

print(reg_model.score(train_x,train_y))

print(reg_model.coef_)
print(reg_model.intercept_)

# prediction 
pred_y = reg_model.predict(test_x)
# error calculation 
print(mean_squared_error(test_y,pred_y))




































































