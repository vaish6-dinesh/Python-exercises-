# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:16:46 2020

@author: Vaish
"""

# Functions  
# Function is  used to perform a specific calculation and return value.
# Syntax for the function defination.
# def function_name(arguement):
# python statements
# return variable;

#Note :- after first line of function defination, second line start with 
# other space, this is called as indent, do not remove this space
# this space is used to start and end function body.

# Once you define function, you can call it multiple time to perform task
# and get result with different values.

# function_name(values)

# 70% of any project will be done using functions.

# write a function to add 2 number

def total_of_2No(x,y):
    total=x+y
    return total;

total_of_2No(10,20)
total_of_2No(-100,90)

# Write a python function to find the total amount to be paid by customer, if
# he get 10% disccount on his purchase amount.

def discount(x,y):
    total= x*y/100
    final_amt= x-total
    return final_amt;

discount(100,10)

# Scope of Variable 
# 1. Local Variable - variable created and used within function.
#                       you cannot use this variable outside the function
#2. Global variable - variable created outside the function and you can use 
#                       it any where

# Here discount and final are local variable
# I want to know the discount also the discount value

final_amt,discount = get_final_amt(100,20)
print(final_amt,discount)

# can we use global variable within function?
#  Example 
 
inc=10

def value_after_in(value):
    new_value=value+value*(inc/100)
    return new_value;

value_after_in(100)

inc=20
value_after_in(100)

# Class assignment
# write python funnction to find a given number is even or odd ?

def iseven(num):
    if (num %2==0):
        print("even")
        return;
    print("odd")
    return;
    
iseven(5)
    

# in this program, we have used if staement, which is a part of
# conditional making statement 
# conditional staements
# 1 if
# 2 while
# 3 for

# why we call it conditional staement 

# if statements
# type - 1
# if (condition): action1

# type 2
# if(condition):
# action1
# actionN
# new statement 

# type 3
# if (conditional):
# action1
# elseif (condition2):
# action2
# else:
# action3


# Class Assignment 

# Write python function to find square and square root of user given 
# value if user value is  above 0 but below 10


# write python function to find the discount percentage given to customer
# based on below condition
# buy 1 30%
# buy2 40%
# buy >2 - 50%


# * to multiply
# ** to square root

def get_value(x):
    sqr=0;sqrrt=0
    if ((x>0) & (x<10)):
        sqr= x*x
        sqrrt= x**(1/2)
    return sqr,sqrrt;

get_value(15)
get_value(2)




































































