# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:34:31 2022

@author: DISRCT
"""
import pandas as pd
tituloMsc = []
anoMsc = []

while True:
    titulo = str(input("Digite o titulo da musica: "))
    if titulo == '':
        break
    else:
        ano = int(input("Digite o ano da musica: "))
    tituloMsc.append(titulo)
    anoMsc.append(ano)
    
musica = {"Músicas": tituloMsc, "Ano lançamento": anoMsc}
df = pd.DataFrame(musica)
media = df["Ano lançamento"].mean()
print(df[df["Ano lançamento"] > media])
