# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:18:13 2022

@author: DISRCT
"""

import numpy as np
a = np.array ([[3,1,2],[7,6,9],[6,4,3]])
impar = (a % 2 != 0)
b = a[impar]
print("Os números impares da matriz são:", b)