# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:15:37 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('tips.csv', sep=';')

x = tips['total_bill']
sns.distplot(x)

sns.jointplot (x='total_bill', y='tip', data = df, color='purple')