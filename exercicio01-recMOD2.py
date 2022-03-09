# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

#--------------EXERCÍCIO 01--------------
import numpy as np
import random as rd

array = np.floor(10*np.random.random((7,7)))
print("Array alearório")
print(array)

x = True 
y = False
maior3 = np.where(array > 3, x, y)
menor8 = np.where(array < 8, x, y)

if maior3 == True:
    array[-1]
elif menor8 == True:
    array[-1]
    
print(array)
    