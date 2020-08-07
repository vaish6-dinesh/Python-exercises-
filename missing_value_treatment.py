# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:01:49 2020

@author: Vaish
"""

# Lamda functions 

# class assignment 

mylist=[10,20,30,40,50]
# increment each value of mylist by 5
mylist=[10,20,30,40,50]

newlist=[]
for i in mylist:
    newlist.append(i+5)
print(newlist)

# or

i=0
for e in mylist:
    e=e+5
    mylist[i]=e
    i+=1
    
print(mylist)

# lambda function to perform the task 
# lambda function - is used to create temporary file 
# lambda function will have arguements and calculations 

# syntax 
lambda args:calculation
f1=lambda x:x+5 
f1(10)

# Map Functions - it is used to perform calculation to each value in the list 
# using the lambda function 

new_list=list(map(lambda x:x+5,mylist))
print(new_list)

# filter function - it is used to create the subset from the list based on given
# conditions 

new_list=list(filter(lambda x:x>30,mylist))
print(new_list)

# class assignment 
# create a new list my taking only odd values from the given list 
mylist2=[2,3,4,5,6,7,8,9]
for num in mylist2:
   if  num % 2 != 0:
       print(num, end = " ")

 nwlist=list(filter(lambda x: x % 2 != 0,mylist2))
 print(nwlist)

# reduce function it is used to reduce given list in single value 
from functools import reduce 
total=reduce(lambda x,y:x+y,new_list)
print(total)


# Missing value detection and treatment 

# =============================================================================
#  when you extract data from different data sources you will get 
#  nan as well if there is no data present in source location 
# =============================================================================
 
# nan = Not an Number and it is taken a missing value 
 
# =============================================================================
#  if you rae getting value such as "?",.(dot) or blank then 
#      these are not taken as missing value, you need to replace all
#      the value by NaN or nan 
# =============================================================================
     
# =============================================================================
#      How to find the missing value in data?
#      
#      1. np.isnan(data['varname']).sum() - gives count of missing value
#      in given variable 
#      
#      2. data.isnull().sum() - gives count of the missing value of all 
#      variables of given dataframe 
#      
#      Your function will return the missing value if you have missing value 
#      value data. so it is very important that you should go for the 
#      treatment 
# =============================================================================
          
# =============================================================================
#      Missing value treatment 
#      1. Drop missing value - data.dropna(axis=0) - is used for large dataset 
#      all rows which has missing value will be droped 
#      
#      2. Replace missing value with the previous value or next value - used 
#      for character value :
#          data.fillna(method="bfill")
#          data.fillna(method="pad")
#          
#      3. Replace missing value with the given value - used as per business 
#      logic 
#          data.replace(np.nan,value)
#      
#      4. Replace missing value with median value - used for numeric value 
#         data.fillna(data.median())
# =============================================================================

import numpy as np 
import pandas as pd 

data=pd.DataFrame(np.random.rand(10,4),columns=list('ABCD'))
print(data)

data.iloc[2:3,0]=np.nan
data.iloc[3:6,1]=np.nan
data.iloc[5:9,2]=np.nan

print(data)

# missing value in C column 
np.isnan(data['C']).sum()

# missing value in all the column 
data.isnull().sum()

# missing value treatment 
# dropping missing value 
data.dropna(axis=0)

# replace the missing value with previous value 
data.fillna(method="pad")

# replace the missing value with 1
data.replace(np.nan,1)

# replace missing value with median 
data.fillna(data.median())

# Assignment 
# class assignment 

location="G:/spyder/Python Part 2 ClassNotes/Class 9/"

dataset = pd.read_table(location+'pima-indians-diabetes.data.txt',
                        sep=",",skiprows=12,header=None)
dataset.shape

# mark zero value as missing value or NaN
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, np.NaN)

# =============================================================================
#   Perform following on given dataset
#   1. Variable 1- replace missing value with previous value 
#   2. variable 2 - replace missing value with 40
#   3. variable 3 - replace the missing value with median 
#   4. variable 4 - drop this variable
#   5. variable 5 - drop missing value observation
# =============================================================================

dataset.isnull().sum()

dataset[1]=dataset[1].fillna(method='pad')
dataset[2]=dataset[2].replace(np.nan,40)
dataset[3]=dataset[3].fillna(dataset[3].median())

# If variable as more than 40% missing value then drop that table 

dataset2=dataset.drop([4],axis=1)
dataset3=dataset.dropna(axis=0) # always do this in last step of data cleaning
dataset3















































