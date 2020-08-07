# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:13:35 2020

@author: Vaish
"""

# =============================================================================
#   Significance Test - is used to test our assumption related to popullation 
#   from given sample 
#   assumption will be related to mean (average) value of popullation 
# =============================================================================
  
# =============================================================================
#   H0(null hypothesis) - is our assumption 
#   H1(alternative hypothesis) - is our opposite hypothesis 
# =============================================================================
  
# what is the average age of people staying in Bangalore? take a guess
  
#  H0 mean age = 30
#  H1 mean age != 30
  
#  to test our assumption we need a sample data with their age value 


sample=[40,24,33,39,38,33]

import numpy as np 

xbar = np.mean(sample);xbar
s = np.std(sample)
stderror = s/np.sqrt(len(sample)-1)
assumed_mean = 30
t = (xbar - assumed_mean)/stderror
df= len(sample)-1

from scipy import stats 

stats.t.ppf(1-0.05,df) # 2.015 

# =============================================================================
#   As t value(1.05) is below the critical region (2.015) , so we accept our 
#   assumption 
#   that is mean value of bangalore is 30
# =============================================================================

stats.ttest_1samp(sample,30)

# statistical result statistic=1.8500095165343353, pvalue=0.12354721380516265
#  if (t-statistical) is less than the t value from the table then accept your :
#      assumption H0
#  or p value is more than 0.05, then accept H0 (this method we always use)

#  T test is used to compare assummed popullation mean with the sample mean value
#   there is two type of t test 
#   ttest_lsamp()
#   1. One sample t test - H0 popullation mean= value
#                          H1 poppulllation mean != value 
#   2. Two sample t test 
#   ttest_ind()
#   2.A Unpaired t test = H0 = mean1 = mean2
#                               mean1 != mean2
   
#   ttest_rel()
#   2.B paired t test H0 : before mean -after mean = 0
#                      H1 : before mean -after meaan !=0
                      
#   in all the test we accept H0 when the p value is more than 0.5(default value)
#   significance_level = 1 - confidence_level

import pandas as pd 
from scipy import stats 

wage_data=pd.read_table("G:/spyder/Python Part 2 ClassNotes/Class 10/Wage.txt",
                        skiprows=26,header=None,skipfooter=6)

wage_data.shape
wage_data.columns

# =============================================================================
#   0 Education : Number of years of education 
#   1 South Indicator variable of southern region
#   2 Sex : Indicator variable for sex(1-female 0-male).
#   3 Experience : Number of years of ecxperience 
# =============================================================================
  
#  Average wage is equal to 15 
#  H0 avg_age=15
#  H1 avg_age != 15
  
stats.ttest_1samp(wage_data[5],15)
# Ttest_1sampResult(statistic=-26.871368673259415, pvalue=3.432186039340737e-101)
# as the p value is less than 0.05 hence we reject H0 and accept H1
# this means average wage is not equal to 15 
# as t statistics is less than 0 (negative), this means we are assuming 
# higher than the actual size 

stats.ttest_1samp(wage_data[5],9)
# Ttest_1sampResult(statistic=0.10820459315650764, pvalue=0.9138741216086457)
# whether there is gender gap in wages 
# conclusion 
# as the p value is more than 0.05 hence we reject H0 and accept H1
# This means that average wage is not equol 9
# as t statistics is close to 0  


# (ii) Whether there is gender gap in usuage 

female_wage=wage_data[wage_data[2]==1][5]
male_wage=wage_data[wage_data[2]==0][5]


# H0 : female wage = male wage 
# H1 : female wage != male wage

stats.ttest_ind(female_wage,male_wage)
# statistics : -4.840066806168903, pvalue=1.7032659492725048e-06
# conclusion 
# as p value is sless than 0.05, so we reject H0, that means female wage is !=
# male wage 

# In case if we have more than two groups, then we are going to use Anova to 
# compare group mean value 

# (v) Whether diffferent occupation havee same average wage 

management_wage=wage_data[wage_data[8]==1][5]
sales_wage=wage_data[wage_data[8]==2][5]
clerical_wage=wage_data[wage_data[8]==3][5]
service_wage=wage_data[wage_data[8]==4][5]
professional_wage=wage_data[wage_data[8]==5][5]
others_wage=wage_data[wage_data[8]==6][5]

#  H0 : different occupation have the same average age 
#  H1 : different occupation do not have the same average age 

stats.f_oneway(management_wage,sales_wage,clerical_wage,service_wage,
               professional_wage,others_wage)

# result : statistic=23.223918389002986, pvalue=4.1217420634431825e-21
#  as p value is sless than 0.05, so we reject H0 this means
# different oocupation have different wage 

# paired t test 

wage_data.groupby(by=8)[5].mean()
# Managementt and professional have highest wage 

# paired t test 
before_staying_in_south_wage=wage_data[wage_data[1]==1][5]
after_staying_in_south_wage=wage_data[wage_data[1]==0][5][:156]

stats.ttest_rel(before_staying_in_south_wage,after_staying_in_south_wage)

# result : statistic=-3.5958453361560885, pvalue=0.00043412138199877803

# Conclusion 

# pvalue is less than 0.05 so we reject H0
# before_staying_in_south_wage is note equal to after_staying_in_south_wage

# Class assignment 
# extract data from brain_size.csv
# can we conclude that the average VIQ of female is equal to average VIQ of male
# If FSIQ is IQ score before trainning and PIQ is IQ score after training,
# can we conclude that training program is not effect?







































































