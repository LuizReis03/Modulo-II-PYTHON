# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 09:10:54 2022

@author: DISRCT
"""

import pandas as pd

df = pd.read_csv('Cars93_miss.csv', usecols=["Manufacturer","Make","Price","MPG.city","Type","Passengers"])
df = df.dropna() # tira todos os NAN das tabelas selecionadas
df = df.loc[df['Passengers'] == 5] # seleciona carros com 5 passageiros
df = df.sort_values(by="MPG.city") # seleciona maiores valores de MPG
df = df.tail(10) # seleciona de baio para cima
df = df.sort_values(by="Price") # selecina os mais baratos
df = df.head(5) # mostra os cinco mais baratos
print(df)