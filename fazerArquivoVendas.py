# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:28:40 2022

@author: DISRCT
"""
import pandas as pd

df = pd.read_csv("Exercício7.csv")
df2 = df[df["Data"] >= 2020]
df2.to_csv("Vendas2020.csv")