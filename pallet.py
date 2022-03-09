# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 08:44:17 2022

@author: DISRCT
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv', sep=';')
sns.set_style("darkgrid")
sns.relplot(x = "total_bill", y = "tip", style="smoker", hue="smoker", palette = "inferno", data = df)
sns.relplot(x = "total_bill", y = "tip",  size='servings', sizes=(15,200), hue="servings", palette = "plasma", data = df)