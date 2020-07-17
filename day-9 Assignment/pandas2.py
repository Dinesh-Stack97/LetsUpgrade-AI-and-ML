# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:18:09 2020

@author: dinesh Pc
"""


import pandas as pd

dataset = pd.read_excel("3. Descriptive Statistics.xlsx", sheet_name = 0)

dattaset8 = dataset['CurrentSalary'].mean()

dataset9 = dataset[['CurrentSalary','After6Months','SalBegin']].mean()

dataset10 = dataset[['CurrentSalary','After6Months','SalBegin']].var()

dataset11 = dataset[['CurrentSalary','After6Months','SalBegin']].std()

dataset12 = dataset[['CurrentSalary','After6Months','SalBegin']].describe()

dataset13 = dataset[['CurrentSalary','After6Months','SalBegin']].sum()

dataset14 = dataset[['CurrentSalary','After6Months','SalBegin']].skew()

#finding outliers
#boxplot

import matplotlib.pyplot as plt

dataset15 = plt.boxplot(dataset.CurrentSalary)

#scatterplot
dataset16 = plt.scatter(dataset.CurrentSalary,dataset.After6Months)

