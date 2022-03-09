# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:15:45 2022

@author: DISRCT
"""

#--------------EXERCÍCIO 03--------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("flights.csv")
mes = df.loc[df['month'] == 'May']
passa = df['passengers']
ano = mes['year']
passaMaio = mes['passengers']

plt.grid(linestyle='-', linewidth=1)
plt.plot(ano, passaMaio, color = 'g', marker = 'o', markerfacecolor='k')
plt.xticks([1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960])
plt.xlabel('Ano')
plt.ylabel('Passageiros')
plt.show()


