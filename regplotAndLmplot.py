# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:32:35 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('tips.csv', sep=';')
sns.regplot(x='total_bill', y='tip', data = df)
sns.lmplot(x='total_bill', y='tip', data = df)