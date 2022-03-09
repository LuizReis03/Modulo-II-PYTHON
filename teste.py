# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:06:52 2022

@author: DISRCT
"""

import pandas as pd
df = pd.read_csv('movies.csv', index_col=["movieId"])

#print(df.describe()) #descrição
#print("\n", df.loc[[10]]) # pega uma posição
#print("\n", df.loc[10:50]) #slice = pega do 10 ate o 50
#print(df.loc[df['genres'] == 'Drama']) #procura pelo genero
#print(df.sort_values(by='title')) #procura em ordem crescente
#print(df.sort_values(by='title', ascending=True)) #procura em ordem crescente
#print(df['Year'].mean()) #media da lista