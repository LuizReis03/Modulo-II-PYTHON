# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:29:20 2022

@author: DISRCT
"""
import pandas as pd
df = pd.read_csv('telefone.csv', index_col=["Ip"])
print(df['Idade'].mean()) #media da lista