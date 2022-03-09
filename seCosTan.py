# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 10:51:50 2022

@author: DISRCT
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, num=100, endpoint = True)
sin = np.sin(x)
cos = np.cos(x)
tan = np.tan(x)
'''
#exercicio 01 - no mesmo grafico
seno = plt.plot(x, sin, label = 'seno', color = 'r')
cosseno = plt.plot(x, cos, label = 'cosseno', color = 'b')
tangente = plt.plot(x, tan, label = 'tangente', color = 'yellow')
plt.legend()


#exercicio 02 - divide em graficos
'''
fig, eixo = plt.subplots(nrows=3, ncols = 1)

eixo[0].plot(x, sin, label = 'seno', color = 'r')
eixo[1].plot(x, cos, label = 'cosseno', color = 'b')
eixo[2].plot(x, tan, label = 'tangente', color = 'yellow')

