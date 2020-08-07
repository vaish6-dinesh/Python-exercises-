# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:56:30 2020

@author: Vaish
"""

import pandas as pd
import numpy as np

sr=pd.Series([1,2,3,4,5])
print(type(sr))
print(sr)



data1=pd.Series({'Title':['Pulp fiction','Inception','Spiderman','Romeo must die','Cold mountain'],
                    'Year':[1994,2010,2002,2000,2003],
                    'Gener':['Crime','Adventure','Action','Action','Drama'],
                    'Rating':[8.9,8.8,7.3,6.1,7.2],
                    'director':['Quentin','Christopher','Sam','Andrej','Anthony']
                    })




data1['director']='Director':['Quentin','Christopher','Sam','Andrej','Anthony']
print(data1)
print(data1.head())
print(data1.tail())
data1[data1['Year'] == '2002'] ['Title']

import numpy as np

Numbers_array1 = np.array([[23, 45, 67, 12, 44],[23, 45, 76, 34, 23]])
Numbers_array2 = np.array([[21, 23, 54, 78, 12],[12, 86, 45, 76, 87]])

New_array = Numbers_array1 + Numbers_array2
print(New_array)

Numbers_array1[1][1:2]
Numbers_array2[1][3:4]

def bonus(x):
    Salary= x*32
    percent= Salary*(100/12)
    return percent,Salary;

bonus(500)

Numbers_array3 = np.array([234, 235, 765, 897, 124, 567, 234, 124])
Numbers_array4 = np.array([980, 786, 980, 654, 456, 654, 786, 234])

Numbers_array3[0:4]
Numbers_array4[0:4]

Numbers_array3.sum()
Numbers_array4.sum()

concat_array = Numbers_array3 + Numbers_array4
concat_array.__len__()

data5=[23,45,24,123,43,23,32,12,76,8,45]
data5.__add__()

def iseven(num=10):
    if (num %2==0):
        print("even")
        return;
    print("odd")
    return;
    
iseven(5)


data5=[23,45,24,123,43,23,32,12,76,8,45]
data5.sort()
data5

def fact(x):
    Factorial= x*(4)(3)(2)(2)
    return Factorial;

fact(5)

#a. What is the difference between List & Tuple? Explain with Example. 
#
#list is a function where in we can the add the data into and it combination of list which is also called as nested list 
#tuple is a function which can we be used to add the same values of data as listed but in tuple we cannot edit the data 



#b. What is the difference between Break & Continue? Explain with Example 
#
#Break and continue are both used in the loopinng statement 
#here in break we can tell the program where it as to be paused 
#continue is a statement which can be used to tell the program from where the program must start 


#c. What is the difference between Pandas Dataframe & Numpy Array? Explain with Example. 
#
#
#Pandas dataframe is used to add the data but the glich in the panda dataframe is that it cannot have a null value
#or missing value hence we need to use the numpy statement (.nan) as to be used
#Numpy array can be formed in the matrix manner over here we can have missing value and as well null values
#but it cannot be achieved in the panadas 






my_list= ['P', 'Y', 'T', 'H', 'O', 'N', 'I', 'S', 'B', 'E', 'S', 'T']

my_list.__len__()


my_list[0:6]

my_newlist = my_list*3

my_list.index('Y')

my_list[9:12]











































