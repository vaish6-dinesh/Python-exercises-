# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:12:30 2020

@author: Vaish
"""

# =============================================================================
#   Outlier - are extremly high and low values are called as outlier values.
#   We need to find outlier in the data and replace it with the median value
#   In case you have left the value as it is, it will give wrong analysis result
#   Because all analysis uses mean value, which is wrong represent mean of 
#   data in case of outlier
# =============================================================================

# =============================================================================
#   How to find outlier?
#   1. Using BOXPLOT method
#   high outlier -> Q3+1.5*IQR
#   low outlier -> Q1-1.5*IQR
# =============================================================================
  
# =============================================================================
#   What is Q3, Q1 and IQR?
#   Q3 - we know 
#   Q1 - we know
#   IQR = Q3-Q1
# =============================================================================
  
# =============================================================================
#  2. Confidence method 
#   mean+-3*std - values above or below is taken as outlier values 
# =============================================================================
  
# =============================================================================
#   Outlier treatment 
#   replace the outlier values with the median vaalue
# =============================================================================

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

np.random.seed(10)
# Random sample will be same with every execution, so we get the same result 

array1 = np.random.normal(100, 10, 200)
# 200 random normalized values with mean 100 and std 10

# method 1 
plt.boxplot(array1)

box_result=plt.boxplot(array1)

out_value=box_result['fliers'][0].get_data()[1]
out_value
len(out_value) # 6 outtliers values

# Method 2 
# mean+- 3*std 

out_values=array1[np.abs(array1-np.mean(array1))>3*np.std(array1)]
out_value







































































