# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:00:02 2022

@author: DISRCT
"""

import pandas as pd
df = pd.read_csv('listatele.csv', index_col=["id"], usecols=("id", "nome"))
print(df.head(8))