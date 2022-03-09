# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 08:32:07 2022

@author: DISRCT
"""

import pandas as pd
df = pd.read_csv('dados.csv', encoding = 'utf-8')

df = df.sort_values(by="preco") 
df = df.loc[df['bairro'] == 'Botafogo']
df = df.loc[df['quartos'] == 2]
df = df.head(5)

print(df)