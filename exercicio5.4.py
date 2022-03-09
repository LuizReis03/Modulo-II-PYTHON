# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 09:28:59 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diamonds.csv', sep=';')

sns.catplot(x = 'color', y = 'price', kind = "swarm" , data = df)
sns.catplot(x = 'clarity', y = 'carat', kind = "swarm", data = df)