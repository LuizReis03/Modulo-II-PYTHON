# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 09:52:02 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diamonds.csv', sep=';')

sns.catplot(x = 'cut', y = 'price', kind = "box" , data = df)
sns.catplot(x = 'cut', y = 'price', kind = "violin", data = df)