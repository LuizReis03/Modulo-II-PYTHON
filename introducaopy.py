# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:03:07 2022

@author: DISRCT
"""

import matplotlib.pyplot as plt

plt.plot([0, 10, 20, 30], label = 'Curva 1')
plt.plot([0, 5, 10, 15], label = 'Curva 2')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('Título do Gráfico')
plt.legend()
plt.show()