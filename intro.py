# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 08:19:25 2022

@author: DISRCT
"""
'''
#BOOLEANO
import numpy as np
my_array = np.full((3,3), True)
print(my_array)
'''

'''
#INDEXAÇÃO
import numpy as np
a = np.array ([[1,2], [3,4], [5,6]])
print(a[0,1])
print(a[[0,1]])
'''
'''
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)

b = np.array = ([0,2,0,1])
print(a[np.arange(4),b])
'''
#booleana
import numpy as np
a = np.array([[1,2], [3,4], [5,6]])
bool_idx = (a > 2)
print(a[a > 2])