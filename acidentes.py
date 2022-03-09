# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:17:13 2022

@author: DISRCT
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('train.csv')
tabela = pd.pivot_table(data=df, values='PassengerId', index='Sex', columns='Survived',
                        aggfunc='count')
bar_1 = tabela[0]
bar_2 = tabela[1]
x_pos = np.arange(len(bar_1))
first_bar = plt.bar(x_pos, bar_1, 0.5, color='b', label='Not survived')
secund_bar = plt.bar(x_pos, bar_2, 0.5, color='y', label='Survived', bottom=bar_1)
plt.xticks(x_pos, ('Female', 'Male'))
plt.legend()

plt.show()
