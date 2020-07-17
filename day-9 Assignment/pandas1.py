# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 08:53:26 2020

@author: dinesh Pc
"""


import pandas as pd
dataset = pd.read_excel("3. Descriptive Statistics.xlsx", sheet_name = 0)

dataset1 = dataset.head()
dataset2 = dataset.head(10)
dataset3 = dataset.head(15)

dataset4 = dataset.tail()
dataset5 = dataset.tail(5)
dataset6 = dataset.tail(10)


dataset7 = dataset.columns

dataset.info

//calculate mean of 1 variable i.e current salary

dattaset8 = dataset['CurrentSalary'].mean()
