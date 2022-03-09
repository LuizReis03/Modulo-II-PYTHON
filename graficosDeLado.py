# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:12:57 2022

@author: DISRCT
"""

import matplotlib.pyplot as plt
import numpy as np

eixo_x = [150,125,200]
palavra = 'ABC'
eixo_y = ['Hspital {}'.format(palavra[a]) for a in range(3)]

plt.barh(eixo_y,eixo_x, height = 0.3, align='center')
plt.grid(True,linestyle = '-', axis='x')
plt.title('Nomero de nascimentos em 3 hospitais', fontsize=15)
plt.xticks(np.arange(0,250,50))
plt.show()