# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:25:03 2020

@author: Vaish
"""

 Assignment 5
# =============================================================================

# =============================================================================
# 1. Create a 1-D array (Numbers_array) with the following values : 
# [23, 56, 23, 34, 56, 76, 52, 51, 63, 82, 73]
# =============================================================================

import numpy as np

Numbers_array = np.array([23, 56, 23, 34, 56, 76, 52, 51, 63, 82, 73])

# a. Find the 4th element of Numbers_array.

Numbers_array[3]

# b. Find the 1st element of Numbers_array.

Numbers_array[0]

# c. Find first four elements of Numbers_array.

Numbers_array[:4]

# d. Create another array with the values [38, 99, 87, 67] and concatenate it 
# with Numbers_array.

Numbers_array1 = np.array([38, 99, 87, 67])
Numbers_array = np.concatenate((Numbers_array,Numbers_array1),axis = 0)
Numbers_array

# =============================================================================
#  2. Create a 2-D array (Numbers_array2) with the following values : 
#  [23, 56, 23, 34, 56, 76][52, 51, 63, 82, 73,58]
# =============================================================================

Numbers_array2 = np.array([[23, 56, 23, 34, 56, 76],[52, 51, 63, 82, 73,58]])
Numbers_array2

# a. Find the length of Numbers_array2.

Numbers_array2.size

# b. Find if 56 is present in Numbers_array2.

if (56 in Numbers_array2): 
    print ("Element Exists")
else:
    print ("Element Does Not Exists")

# c. Find if 99 is present in Numbers_array2.

if (99 in Numbers_array2): 
    print ("Element Exists") 
else:
    print ("Element Does Not Exists")

# =============================================================================
# 3. Create two arrays with the following values :
# array1 = [23, 56, 23, 34, 56, 76, 52, 51, 63, 82, 73]
# array2 = [13, 46, 13, 36, 78, 61, 12, 70, 61, 13, 78]
# =============================================================================

array1 = np.array([23, 56, 23, 34, 56, 76, 52, 51, 63, 82, 73])
array2 = np.array([13, 46, 13, 36, 78, 61, 12, 70, 61, 13, 78])

# a. Add, Subtract, Multiply and Divide array1 and array2.

sum_array = np.add(array1, array2)

sub_array = np.subtract(array1, array2)

mul_array = np.multiply(array1, array2)

div_array = np.divide(array1, array2)

sum_array
sub_array
mul_array
div_array

# b. Find sum and Product of array1.

sum_of_all = np.sum(array1)
pro_of_all = np.product(array1)

# c. Find all the unique value of array2.

array2_uniq = np.unique(array2)

# d. Compare array1 & array2.

compare_array  = np.equal(array1,array2)
compare_array