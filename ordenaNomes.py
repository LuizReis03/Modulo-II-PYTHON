# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:27:28 2022

@author: DISRCT
"""

import pandas as pd
df = pd.read_csv('telefone.csv', usecols=["Ip","Nomes"])
print(df.sort_values(by='Ip')) #mostra a frequencia