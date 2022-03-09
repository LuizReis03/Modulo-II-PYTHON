# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:14:16 2022

@author: DISRCT
"""

#--------------EXERCÍCIO 02--------------
import pandas as pd

df = pd.read_csv("train.csv")
tamanho = len(df)
homens = len(df.loc[df['Sex'] == 'male'])
homens = (100*homens)/tamanho
mulheres = len(df.loc[df['Sex'] == 'female'])
mulheres = (100*mulheres)/tamanho

print("Homens no Titanic:", homens,"%")
print("Mulheres no Titanic:", mulheres,"%")
