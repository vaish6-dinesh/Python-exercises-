# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 08:58:44 2020

@author: Vaish
"""

# =============================================================================
#    Correlation is used to find the relation between two numeric variables 
#    such as height and weight, price and quantity, discount and quantity
# =============================================================================

# =============================================================================
#    Correlation is measured by correlation coefficient (r)
#    r between x and y - covariance between x and y / std of x * std of y
#    covariance between x and y - sum ((xi - xbar)*(yi-ybar))/(n-1)
#    xi - ith value of x, xbar - mean of x 
#    yi - ith value of y, ybar - mean of y 
# =============================================================================
   
# =============================================================================
#    Value of r lies betweeen -1 to +1
#    -ve value - negative correlation - means if one variables increases other 
#                will decrease or vice versa 
#     +ve value - positive correlation - means both variables increases or 
#                 decreses together 
#     zero value - no coorelation 
# =============================================================================
    
# =============================================================================
#     Type of correlation 
#     if absolute value of r :
#         0 - 0.3 - weak correlation 
#         0.3 - 0.5 - moderate correlation 
#         0.5 - 1.0 - strong correlation 
# =============================================================================
        
# =============================================================================
#     correlation test 
#     H0(null hypothesis) - correlation is equal to zero
#     H1(alternate hypothesis) - correlation is not equal to zero
# =============================================================================

# =============================================================================
#   pvalue >= 0.5, we accept H0, else reject H0
#   rejecting H0 means you have to accept H1
# =============================================================================
  
# =============================================================================
#   When we accept H1-> pvalue<0.5
#   5% (or 0.05) - is called as level of significance 
#   (represent area of rejection)
#   if we perform samme test with 100 sample, then 5% sample result will
#   be different from 95% sample.
#   this 5% is standard error because random selection of sample
# =============================================================================

# =============================================================================
#   to calculate p value 
#   mean, std, x
#   z = (x-mean)/std
#   p(z) - this comes from the z table 
#   pvalue = 1-p(z)
# =============================================================================
  
import numpy as np 
from scipy.stats import pearsonr

x=[180,165,157,162,175,153,178,177]
y=[82,52,53,55,80,51,84,100]

np.corrcoef(x,y)
pearsonr(x,y)

# (r - 0.8913930866624138) (pvalue - 0.0029474640292817987)

# =============================================================================
#   conclusion - there is positive strong correlation between x and y.
#   as p value is less than 0.05, so we reject H0, this means correlation
#   is not equal to zero
# =============================================================================

import pandas as pd 

data=pd.DataFrame({'x':x,'y':y})
data['x'].corr(data['y'])  # correlation between x and y 
data.corr()  # correlation matrix

# We can plot the result in the graph by using the following package 
import matplotlib.pyplot as plt
plt.scatter(x,y)

# =============================================================================
#   to understand the graph 
#   if it as low to high value, then it is called positive correlation 
#   if it as high to low value, then it is called negative correlation
# =============================================================================

x = np.random.randint(0,100,1000)
y = x+np.random.randint(0,5,1000)
import matplotlib.pyplot as plt
plt.scatter(x,y)

# Assignment  mpg and weight 

import pandas as pd
import os

os.chdir("G:/spyder/Python Part 2 ClassNotes/Class 8/Assignments") 
os.listdir()

data2=pd.read_excel("Data.xlsx")
data.shape

data2.columns

x=data2['MPG']
y=data2['WEIGHT']

data2=pd.DataFrame({'x':x,'y':y})
data2['x'].corr(data['y'])
data2.corr()

import matplotlib.pyplot as plt
plt.scatter(x,y)


















































