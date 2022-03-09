# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:50:22 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('tips.csv', sep=';')
print(df.corr())
sns.heatmap(df.corr(), annot = True)