# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:50:59 2022

@author: DISRCT
"""

import math

def calculaCirculo(r):
    raio = r**2
    a = math.pi * raio
    return a

valor = float(input("Digite o raio: "))
if valor >= 0:
    a = calculaCirculo(valor)
    a = round(a,2)
    print(a)
else:
    print("Raio inválido")