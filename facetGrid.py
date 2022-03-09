# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:36:54 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('tips.csv', sep=';')

grid = sns.FacetGrid(df, col='time') #Seprado por coluna
grid2 = sns.FacetGrid(df, row='time') #Seprado por linha
grid3 = sns.FacetGrid(df, hue='time') #Seprado por cores

grid.map(plt.hist, 'total_bill')
grid2.map(plt.hist, 'total_bill')
grid3.map(plt.hist, 'total_bill')

