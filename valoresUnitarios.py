# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:12:55 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("company_sales_data.csv")
faceCream = df["facecream"]
faceWash = df["facewash"]
toothpaste = df["toothpaste"]
bathingsoap = df["bathingsoap"]
shampoo = df["shampoo"]
moisturizer = df["moisturizer"]

plt.plot(faceCream, label = 'Face Cream Sales Data', color = 'b', linestyle = '-',
         marker = 'o', linewidth=3)

plt.plot(faceWash, label = 'Face Wash Sales Data', color = 'y', linestyle = '-',
         marker = 'o', linewidth=3)

plt.plot(toothpaste, label = 'ToothPaste Sales Data', color = 'g', linestyle = '-',
         marker = 'o', linewidth=3)

plt.plot(bathingsoap, label = 'BathingSoap Sales Data', color = 'k', linestyle = '-',
         marker = 'o', linewidth=3)

plt.plot(shampoo, label = 'Shampoo Sales Data', color = 'c', linestyle = '-',
         marker = 'o', linewidth=3)

plt.plot(moisturizer, label = 'Moisturizer Sales Data', color = 'm', linestyle = '-',
         marker = 'o', linewidth=3)

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.xlabel('Meses')
plt.ylabel('Lucro Unitario')
plt.savefig('grafico_lucroUnitario')
plt.legend()
plt.show()
