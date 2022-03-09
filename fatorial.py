# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 10:40:58 2022

@author: DISRCT
"""

def fatorial(x):
    if x < 2:
        print("Não existe fatorial de numero menor que 2")
        return False
    else:
        resultado = x
        for i in range(x-1, 0, -1):
            resultado = resultado * i
        return resultado
    
numUsuario = int(input("Digite um numero: "))
calcula = fatorial(numUsuario)
print(calcula)