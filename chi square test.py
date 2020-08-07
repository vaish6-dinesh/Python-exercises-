# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:11:16 2020

@author: Vaish
"""

# Chi-square is used to test between two categorical value

# contigency table 

# xsq = (Ex-obs)^2/Ex 

# Ex = Rt * Ct /total obs
# Rt - row total 
# Ct - column total 

# obs value come from the table

# =============================================================================
#   Chi square test test - is used to find the assumption between two character
#   variable such sex and grade, type and purchase 
#   perform and goodies 
# =============================================================================
  
# =============================================================================
#   Chi-square is calculated using the below formula 
#   xsq = (Ex-obs)^2/Ex 
# =============================================================================
  
# =============================================================================
#   chi square test assumption 
#   H0: there is no association with the given variables 
#   H1: there is association between given variables 
# =============================================================================
  
# =============================================================================
#   Reject H0 if the P value is below 0.05 and accept H1 that means given 
#   variable as association 
# =============================================================================
  
# =============================================================================
#   DOF - Degree Of Freedom 
#   DOF = (r-1)*(c-1)
#   r - number of rows in contigency table 
#   c - number of columns in the contigency table 
#   
#   Contigency table - is cross table of given variables 
# 
# =============================================================================

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# test of association 

path="G:/spyder/Python Part 2 ClassNotes/Class 10/"
Hair_Eye_Color=pd.read_table(path+"Hair_Eye_Color.txt",
                             delim_whitespace=True,header=0)
print(Hair_Eye_Color.head())

cont_table=pd.pivot_table(Hair_Eye_Color,values=['n'],
                             index=['Hair'],columns=['Eye'],
                             aggfunc=np.sum)

table=cont_table.replace(np.NaN,0)

# table = np.array(table)
# table2 = table1.reshape(15,)

# H0 there no association between hair and eye 
# H1 there is association between hair and eye 

chsq, pvalue, dof, exp=chi2_contingency(table)
print(chsq)
print(pvalue)
print(dof)
print(exp)































