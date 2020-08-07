# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:02:17 2020

@author: Vaish
"""

# =============================================================================
# #pip install numpy in the anaconda prompt 
# # What is a package?
# # pacakage are compressed file to store different objects and functions 
# # in order to use function or package you have to first install it 
# # and import the package in every session of python 
# # How to install the package?
# # you can use the command promt to install the package 
# # command to install the package is - pip install package_name
# # or you can use the GUI for installation 
# # Go to anacondo navigator >> environment >> select not installed 
# # search package name >> select desired package name and apply
# # Your system should must be connected to the internet 
# # You have install the package only one time 
# # How to use package functions 
# # In order to use the package functions, we have to import in every python session
# # with the below given code
# # import package_name as alias 
# # import for all function of the given package 
# # from package_name import function_name 
# # for single function of the given package  
# =============================================================================

import numpy as np

# numpy is used for numeric calculation.
# it creates an object like matrix which store only similar kind of value.

# numpy is like salt in the food.

data1=np.array([10,20,30,40,50])
type(data1)
data1.shape

data2=np.array(np.arange(1,13))
data2
data2.shape

data2=data2.reshape([3,4])
# [coulmn,row], reshape is used to reshape the row and coulmn
data2.shape
data2

# extraction 
data1[2:4]

data2[2][1:3]  # nested list style

data2[2,1:3] # array style

# manipulation 

# =============================================================================
# # Terminology 
# # rows - index or observations
# # columns - columns or variables
# # table - dataset or dataframe 
# =============================================================================
# =============================================================================
# 
# # Class assignment 
# # 1. Create an array with alues 2 to 11 with shape 2,5
# 
data3=np.array(np.arange(2,12))
data3
data3.shape

data3=data3.reshape([2,5])
data3.shape
data3
# 
# =============================================================================

# 1.add 

np.add(data3,10)
np.sum(data3)

np.sum(data3,axis=0)
# axis-0 means index value sum,this will give coulmn wise total

np.sum(data3,axis=1)
# axis=1 means coulmn value sum, this will give row wise total 

# 2. delete 

data1
data1_new=np.delete(data1,[2])
data1_new 

# 3.transpose 
np.transpose(data3)

# 4. Sort 
data4=np.array([10,15,12,18,13,17])
np.sort(data4) # ascending order sort 
# how sort in descending order assignment question search in google 
data5=-np.sort(-data4)
data5

# statistical functions 
np.mean(data4)
np.median(data4)
np.var(data4)
np.std(data4)
np.quantile(data4,[0.25,.50,.75])


# random number generation using numpy 
np.random.rand(10,20) # 10 rows and 4 coulmns random value 

np.random.randint(10,20,10) # 12 random integer value between 10 and 20 
np.random.normal(10,5,12) # 12 normaly distributed data with mean 10 and std 5.






























































































