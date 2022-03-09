# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:37:34 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("company_sales_data.csv")
print(df)
bathing = df["bathingsoap"]
faceWash = df["facewash"]
mes = df["month_number"]

fig, eixo = plt.subplots(nrows=2, ncols = 1)

eixo[0].plot(mes, bathing, color='b', marker='o', label="BathingSoap")
eixo[1].plot(mes, faceWash, color='r', marker='o', label="FaceWash")

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.xlabel('Month number')
plt.ylabel('Sales units in number')
