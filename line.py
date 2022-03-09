# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 09:01:13 2022

@author: DISRCT
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('firearm.csv', sep=',')

sns.set_style("darkgrid")
sns.relplot(x = 'month', y = 'permit', kind = 'line', style="state", hue = "state", palette = "inferno", ci = None, data = df)