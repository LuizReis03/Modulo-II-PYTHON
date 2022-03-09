# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 08:40:44 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("company_sales_data.csv")

faceCream = df["facecream"]
faceWash = df["facewash"]
mes = df["month_number"]

plt.bar(mes +0.2, faceWash, width=0.3, color='c', label = 'Face Wash Sales Data')
plt.bar(mes -0.2, faceCream, width=0.3, color='b', label = 'Face Cream Sales Data')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.grid(True, linestyle='--')
plt.xlabel('Month Number')
plt.ylabel('Sales unites in number')
plt.legend(loc = 'upper left')
plt.savefig("grafico_Cremes")
plt.show()