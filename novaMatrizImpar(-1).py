# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:31:25 2022

@author: DISRCT
"""

import numpy as np
a = np.array ([[3,1,2],[7,6,9],[6,4,3]])
impar = (a % 2 != 0)
a[impar] = -1
print("Os números impares da matriz são:", a)