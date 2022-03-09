# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:16:04 2022

@author: DISRCT
"""

#--------------EXERCÍCIO 04--------------
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-1, 2, num=100, endpoint = True)
x = np.arange(math.radians(-360), math.radians(360),0.1)
sin = np.sin(x)
cos = np.cos(x)

fig, eixo = plt.subplots(nrows=2, ncols = 1)
eixo[0].grid(linestyle='-', linewidth=1)
eixo[1].grid(linestyle='-', linewidth=1)
eixo[0].plot(x, sin, label = 'Cosseno de x', color = 'r')
eixo[1].plot(x, cos, label = 'Seno de x', color = 'b')
fig.tight_layout() 
plt.legend()
plt.show()