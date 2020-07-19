# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:47:59 2020

@author: dinesh Pc
"""


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

dataset1 = pd.read_csv("general_data_set.csv")

dataset1.head()

daataset2 = dataset1.isnull()

dataset3 = dataset1.duplicated()

dataset4 = dataset1.drop_duplicates()

#univarient analysis

dataset5 = dataset1[['Age','Attrition','BusinessTravel','Department',
                     'DistanceFromHome','Education','EducationField',
                     'Gender','JobRole','MaritalStatus',
                     'MonthlyIncome','NumCompaniesWorked',
                     'PercentSalaryHike',
                     'TotalWorkingYears','TrainingTimesLastYear',
                     'YearsAtCompany','YearsSinceLastPromotion',
                     'YearsWithCurrManager']].describe()
#median
dataset6 = dataset1[['Age','Attrition','BusinessTravel','Department',
                     'DistanceFromHome','Education','EducationField',
                     'Gender','JobRole','MaritalStatus',
                     'MonthlyIncome','NumCompaniesWorked',
                     'PercentSalaryHike',
                     'TotalWorkingYears','TrainingTimesLastYear',
                     'YearsAtCompany','YearsSinceLastPromotion',
                     'YearsWithCurrManager']].median()
#mode
dataset7 = dataset1[['Age','Attrition','BusinessTravel','Department',
                     'DistanceFromHome','Education','EducationField',
                     'Gender','JobRole','MaritalStatus',
                     'MonthlyIncome','NumCompaniesWorked',
                     'PercentSalaryHike',
                     'TotalWorkingYears','TrainingTimesLastYear',
                     'YearsAtCompany','YearsSinceLastPromotion',
                     'YearsWithCurrManager']].mode()

#var
dataset8 = dataset1[['Age','Attrition','BusinessTravel','Department',
                     'DistanceFromHome','Education','EducationField',
                     'Gender','JobRole','MaritalStatus',
                     'MonthlyIncome','NumCompaniesWorked',
                     'PercentSalaryHike',
                     'TotalWorkingYears','TrainingTimesLastYear',
                     'YearsAtCompany','YearsSinceLastPromotion',
                     'YearsWithCurrManager']].var()

#skew
dataset9 = dataset1[['Age','Attrition','BusinessTravel','Department',
                     'DistanceFromHome','Education','EducationField',
                     'Gender','JobRole','MaritalStatus',
                     'MonthlyIncome','NumCompaniesWorked',
                     'PercentSalaryHike',
                     'TotalWorkingYears','TrainingTimesLastYear',
                     'YearsAtCompany','YearsSinceLastPromotion',
                     'YearsWithCurrManager']].skew()

#kurt

dataset10 = dataset1[['Age','Attrition','BusinessTravel','Department',
                     'DistanceFromHome','Education','EducationField',
                     'Gender','JobRole','MaritalStatus',
                     'MonthlyIncome','NumCompaniesWorked',
                     'PercentSalaryHike',
                     'TotalWorkingYears','TrainingTimesLastYear',
                     'YearsAtCompany','YearsSinceLastPromotion',
                     'YearsWithCurrManager']].kurt()

dataset11 = dataset1[['Age','Attrition','BusinessTravel','Department',
                     'DistanceFromHome','Education','EducationField',
                     'Gender','JobRole','MaritalStatus',
                     'MonthlyIncome','NumCompaniesWorked',
                     'PercentSalaryHike',
                     'TotalWorkingYears','TrainingTimesLastYear',
                     'YearsAtCompany','YearsSinceLastPromotion',
                     'YearsWithCurrManager']].describe()

dataset12 = plt.boxplot(dataset1.Age)

dataset13 = plt.boxplot(dataset1.MonthlyIncome)

dataset14 = plt.boxplot(dataset1.YearsAtCompany)





