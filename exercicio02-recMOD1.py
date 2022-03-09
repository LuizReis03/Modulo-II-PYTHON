# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:36:13 2022

@author: DISRCT
"""

#---------------PROVA---------------
#---------------EXERCÍCIO 02---------------

lista = []

while True:
    try:
        numUsuario = int(input("Digite um valor: "))
        mult = numUsuario * 2
        lista.append(mult)
        print(lista)
        pergunta = input("Deseja continuar? (s/n) ")
        
        if pergunta == 's' or pergunta == 'S':
            continue
        elif pergunta == 'n' or pergunta == 'N':
            print(lista)
            break
        elif pergunta != 'n' or pergunta != 'N' or pergunta != 's' or pergunta != 'S':
            print("Verifique o que foi digitado...")
            break
        
    except:
        print("Verifique o que foi digitado...")