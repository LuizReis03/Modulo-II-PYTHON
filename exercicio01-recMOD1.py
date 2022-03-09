# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:25:24 2022

@author: DISRCT
"""

#---------------PROVA---------------
#---------------EXERCÍCIO 01---------------
def verificaPalavra(x):
    invertido = x[::-1]
    
    print("{} <- PALVRA AO CONTRÁRIO". format(invertido.lower()))

    
palavra = str(input("Digite uma palavra: "))
verificaPalavra(palavra)