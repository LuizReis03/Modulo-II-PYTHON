# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:19:39 2022

@author: DISRCT
"""

import pandas as pd
df = pd.read_csv('telefone.csv', index_col=["Ip"])
tamanho = df.shape
linhas = tamanho[0]
colunas = tamanho[1]
metade = int(linhas/2)
print(df.tail(metade))