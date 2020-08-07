# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 08:53:30 2020

@author: Vaish
"""

# =============================================================================
#  Descriptive Statistics - is used to find how given data is distributed 
#  and various statistical values.
# =============================================================================
 
# =============================================================================
#  Descriptive statistics - is defined with four terms
#  1. Central Tendancy - Mean,Meadian,Mode 
#  2. Dispersion - variance,std,range,inter quantile range
#  3. Skewness -  spread of values along with mean 
#  4. Kurtosis - peakness of data at mean.
# =============================================================================
 
# =============================================================================
#  Mean - It is a average value, sum of all values/no of values.
#  Meadian - It is middle most value after sorting data in ascending order.
#  Mode - It most frequently occuring value, values which comes maximum time
#         in the dataset
# =============================================================================

import pandas as pd
import numpy as np 
import os

os.chdir("G:/spyder/Python Part 2 ClassNotes/Class 7/Assignments") 
os.listdir()

data3.columns
data3=pd.read_excel("sales.xlsx")
data3.shape

data3['Sales'].mean() # value based
data3['Sales'].mode() 
data3['Sales'].median()  # position based

# =============================================================================
#  variance - average deviation from the eman value 
#              sum(obs-mean(obs))^2)/no of obs-1
#  std - square root of average deviation.
#  range - difference between max and min
#  IQR - difference between Q3 and Q1
#          Q3 - 3rd Quantile value, Q1 - 1st Quantile value
#  Quantile means divide the data into four equal parts after sorting
#  First 25% data - Q1 - 25%
#  Second 25% data - Q2 - 50%
#  Third 25% data - Q3 - 75%
# =============================================================================

# =============================================================================
#  Why we need to calculate the mean median and mode ?
#  This will help us to identify our potential customer or target 
#  if a new customer/client will come whoes age is close to average age :
#  of your right customer, then you can put extra effort to make him 
#  buy the producct from you
# =============================================================================

data3['Sales'].var()
data3['Sales'].std()
data3['Sales'].max()-data3['Sales'].min()
data3['Sales'].quantile([.25,.5,.75])

# =============================================================================
#  Why we need this?
#  this will help us to customer range in what range my customer needs varies
#  and help us to understand their requirements 
# =============================================================================
 
# Skewness - defines the spreadness of data alone with the mean.
#               number observation above or below the mean 
# =============================================================================
#   Skewness - 0 - if we have equal number of observation 
#   Skewness - -ve - if we have more number of observation below mean 
#   Skewness - +ve - if we have more number of above mean
# =============================================================================
  
data3['Sales'].skew()

# =============================================================================
#   Kurtosis - defined the peakness of graph at mean value
#   Kurtosis - 0 - if peakness of the graph is equal to normal distribution 
#   Kurtosis - -ve - if the peakness of the graph is less than normal
#                   distribution
#   Kurtosis - -ve - if the peakness of the graph is greater 
#                   than normal distribution
# =============================================================================

data3['Sales'].kurt()

import seaborn as sns
sns.distplot(data3['Sales'],hist=True,kde=True)

# To get basic descriptive statistics 
data3.describe()

# read what is coorelation 























































