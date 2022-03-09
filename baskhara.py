# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 08:43:44 2022

@author: DISRCT
"""

def baskhara(a, b, c):
    if a == 0:
        print("\nNão é uma equeacão do 2 grau, pois a é igual a 0")
        return 0
        
    delt = (b ** 2) - 4 * a * c
    if delt < 0:
        print("\nNão há raízes reais!")
        return 0
        
    elif delt > 0:
        x1 = (-b + delt ** (1 / 2)) / (2* a)
        x2 = (-b - delt ** (1 / 2)) / (2* a)
        return x1, x2
        
    elif delt == 0:
       x1 = (-b + delt ** (1 / 2)) / (2* a)
       return x1
    
numA = int(input("Digite o valor de a: "))
numB = int(input("Digite o valor de b: "))
numC = int(input("Digite o valor de c: "))

print(baskhara(numA, numB, numC))




        
    