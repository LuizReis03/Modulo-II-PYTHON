# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 08:14:41 2022

@author: DISRCT
"""

import numpy as np
import random as rd

array = np.random.randint(50, size=(4, 4))
print(array)
             
par = (array % 2 == 0)
array[par] = 0

print("\n", array)
