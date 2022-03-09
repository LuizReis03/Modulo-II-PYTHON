# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 09:50:04 2022

@author: DISRCT
"""

#--------------EXERCÍCIO 05--------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("flights.csv")
mes = df.loc[df['month'] == 'January']
sns.barplot(x=mes['year'], y=df['passengers'], data = df)
plt.yticks([0,100,200,300,400])
