# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 08:48:45 2020

@author: Vaish
"""

# =============================================================================
# 
#   Pandas package - is used for general purpose task such as storing 
#   data in the form of table, sorting of data, by group calculation etc.
#   All sort of basic Exploration Data Analysis(EDA) will be performed 
#   by pandas package.
#   in order to use the package, we need to install it first,
#   Then import it in the current session.
#   Ananconda has a pre installed pandas package, no need to install it.
#   
# =============================================================================

import pandas as pd

# =============================================================================
# #  pandas as two type of object - Series, dataframe
# #  series - is used to store similar type of values and it is 
# #  one dimensional array 
# #  dataframe - is used to store different types of values in 
# #  spreadsheet format, it is two dimensional array.
# 
# =============================================================================

sr=pd.Series([1,2,3,4,5])
print(type(sr))
print(sr)

data1=pd.DataFrame({'x':[101,102,103,104],
                    'y':['a','b','c','d'],
                    'z':['M','F','M','F']
                    })
print(type(data1))
print(data1)

# note - each coulmn should must have equal number of values 

data2=pd.DataFrame({'x1':[100,200,300,400],
                    'x2':'blr',
                    'x3':'India'
                    })
print(type(data2))
print(data2)


# In case of list value for coumn, you need to create equaal number of values

data3=pd.DataFrame({'x1':[100,200,300,400],
                    'x2':['blr','chn']*2,
                    'x3':['India']*4
                    })
print(type(data3))
print(data3)

# For using missing value we have use the function numpy 
# np.nan is used to create the missing value.
# nan - not a number

import numpy as np

data4=pd.DataFrame({'x1':[100,200,300,400],
                    'x2':['blr',np.nan,'chn','mum'],
                    'x3':['India']*4
                    })
print(type(data4))
print(data4)

# =============================================================================
#   class assignment :
#   create a dataframe called employee with 10 rows and 4 coulmn 
#   coulmn and its values are as follows 
#   id A101,A102,A103.........
#   Name - ravi mona rabina mohan ganesh raju roja ramesh himani manish
#   sexx - f and M
#   
# =============================================================================
  
data5=pd.DataFrame({'Id':['A101','A102','A103','A104','A105','A106','A107','A108','A109','A110'],
                    'Name':['ravi','mona','rabina','mohan','ganesh','raju','roja','ramesh','himani','manish'],
                    'sex':['M','F','F','M','M','M','F','M','F','M'],
                    'Age':np.random.randint(25,28,10),
                    'Salary':np.random.randint(20000,40000,10)
                       })
print(type(data5))
print(data5)

# extraction 
data5['Name']
data5['Name'][0:5]
data5[['Name','Age']]
data5[['Name','Age','Salary']]\

data5[0:5]

# what is the salary of mohan 
data5[data5['Name'] == 'mohan']['Salary']

# what is the salary of ganesh 
data5[data5['Name'] == 'ganesh']['Salary']

# google search question 

# to get some basic  information about data frame 
print(data5.head()) # give top 5 row
print(data5.tail()) # give bottom 5 row
print(data5.shape) # give dimesnion of data
print(data5.columns) # give the column name of dataframe 

# data frame manipulation 
# 1. adding new coulmn 
data5['HRA']=data5['Salary']*0.30
print(data5)

# 2. dropping columns
data5.drop(['Id'],axis=1,inplace=True)
print(data5)

# 3. Transposing of the data
data5.T

# 4. Sorting of the data frame
data5.sort_values(by='Salary')
# sorting of data in descending order 

# 5. group bby calculation 
# find the average salry for each group of sex 
data5.groupby(by='sex')['Salary'].mean()

# find the average HRA for each group of sex 
data5.groupby(by='sex')['HRA'].mean()

# find total HRA given to the employees
data5['HRA'].sum()

print(data5.shape)


















































































