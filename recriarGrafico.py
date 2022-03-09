# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:50:35 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("company_sales_data.csv")
meses = df["month_number"]
valores = df["total_units"]
plt.plot(meses, valores, label = 'Mes', color = 'r', linestyle = '--',
         marker = 'o', markerfacecolor='black', linewidth=3)
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.yticks([1000, 20000, 30000, 40000, 50000])
plt.xlabel('Meses')
plt.ylabel('Lucro Total')
plt.title('Título do Gráfico')
plt.legend()
plt.show()
