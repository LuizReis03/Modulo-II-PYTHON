# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 09:08:47 2022

@author: DISRCT
"""

def anagrama(x, y):
    x = sorted(x)
    y = sorted(y)
    print(x)
    print(y)
    if x != y: 
        return False
    else:
        return True
          
palavra1 = input("Digite a primeria palavra: ")

palavra2 = input("Digite a segunda palavra: ")

resultado = anagrama(palavra1, palavra2)
print(resultado)