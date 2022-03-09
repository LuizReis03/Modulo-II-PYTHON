# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:11:09 2022

@author: DISRCT
"""

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("company_sales_data.csv")

eixoX = df["month_number"]
eixoY = df["toothpaste"]

plt.scatter(eixoX, eixoY, color='b', label = 'Tooth paste Sales data')
plt.grid(linestyle="--")
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.xlabel('Month Number')
plt.ylabel('Number of units Said')
plt.legend(loc = "left upper")
plt.show()