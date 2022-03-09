# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:28:22 2022

@author: DISRCT
"""

import pandas as pd
df = pd.read_csv('telefone.csv', usecols=["Nomes","Idade"])
print(df["Idade"].value_counts()) #mostra a frequencia
