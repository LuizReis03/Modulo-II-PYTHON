# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 08:17:58 2022

@author: DISRCT
"""

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('company_sales_data.csv')

x = df["month_number"]
y = df["total_units"]
plt.bar(x, y, width=0.8, color='b', ec='black', align='center')
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.grid(True, linestyle='--')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.savefig('grafico_vendas')
plt.show()