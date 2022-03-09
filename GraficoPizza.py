# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:25:14 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("company_sales_data.csv")

faceCream = df["facecream"].sum()
faceWash = df["facewash"].sum()
toothpaste = df["toothpaste"].sum()
bathingsoap = df["bathingsoap"].sum()
shampoo = df["shampoo"].sum()
moisturizer = df["moisturizer"].sum()

lista = np.array([[faceCream], [faceWash], [toothpaste], [bathingsoap], [shampoo], [moisturizer]])
label = ['FaceCream', 'FaceWash', 'ToothPaste', 'Bathingsoap', 'Shampoo', 'Moisturizer']
plt.figure(figsize = (5.9 , 5.9))
plt.pie(lista, autopct='%1.1f%%', colors = ['tab:gray', 'tab:blue', 'g', 'c', 'y', 'm'])
plt.xlabel('Sales data')
plt.legend(label, loc = 'lower left')
plt.show()
