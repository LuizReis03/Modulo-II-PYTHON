# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:41:44 2022

@author: DISRCT
"""

#---------------PROVA---------------
#---------------EXERCÍCIO 03---------------
while True:

    termos = int(input("Digite o número de termos desejado: "))
    soma = 0
    for i in range(termos):
        soma = soma + 1 /(2* i)
        break
    print(soma)
