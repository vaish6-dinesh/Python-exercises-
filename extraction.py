# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 09:07:44 2020

@author: Vaish
"""

# Extraction of data into python from different source

import pandas as pd
import os

# Set working directory location

os.chdir("G:/spyder/Python Part 2 ClassNotes/Class 7/Assignments") 
os.listdir()

# Extraction from text file :- pd.read_table() 
data1=pd.read_table("company.txt",sep="/",header=None)
data1.shape


# Extraction from csv files :- pd.read_csv()

data2=pd.read_csv("crabtag.csv")
data2.shape

# Extraction from excel file :- pd.read_excel()
data3=pd.read_excel("sales.xlsx")
data3.shape

# Extraction from sas file :- pd.read_sas()
data4=pd.read_sas("cars.sas7bdat")
data4.shape

# Class assignment 
# 1 How to read sheet2 data from excel 
data3A=pd.read_excel("sales.xlsx",sheet_name="Sheet1")
data3A.shape

data3B=pd.read_excel("sales.xlsx",header=None)
data3B.keys()


# Extraction from databse file -
# Sql server oracle data teradata mysql nosql mangodb etc

import pyodbc
# =============================================================================
#  You have to create a DSN(Data Source Name)
#  In oredr to extract data from database, we need DSN
#  We have to first create DSN  
# =============================================================================

# =============================================================================
#  How to create user DSN
#  goto control panel->select system and security-> administrative tools
#  -> Data source (ODBC)-> user DSN->click add-> in popup window
#  give name to DSN (it will be used in python code) and server name
#  select finish->next->change default databse to database which 
#  you want extract->next->next->test data sorce connection 
#  click ok to close all windows 
# =============================================================================


conn=pyodbc.connect(dsn = 'Python')
data5=pd.read_sql('select * from spt_monitor',conn)
print(data5)












































