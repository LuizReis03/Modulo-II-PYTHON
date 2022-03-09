# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 09:57:57 2022

@author: DISRCT
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

listaPar = []
listaImpar = []

#pede numero do usuario até inserir 0 -  verifica se é par ou impar
while True:
    try:
        df = int(input("Digite um número: "))
        if df == 0:
            break
        elif df % 2 == 0:
            listaPar.append(df)
        else:
            listaImpar.append(df)
    except:
         print("Verifique o que foi digitado!")
        
#atribui o tamanho das listas nas variaveis
tamanhoPar = len(listaPar)
tamanhoImpar = len(listaImpar)

#cria uma nova lista com os tamanhos
listaPizza = [tamanhoPar, tamanhoImpar]

#cria o gráfico
label = ['Par', 'Impar']
plt.pie(listaPizza, autopct='%1.1f%%', colors = ['tab:gray', 'tab:blue'])
plt.legend(label)
plt.savefig('graficoParOuImpar')
plt.show()

