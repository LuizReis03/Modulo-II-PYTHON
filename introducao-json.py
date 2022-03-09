# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:24:59 2022

@author: DISRCT
"""

import json

x = '{"Nome": "João", "Idade": "20"}'

y = json.loads(x)
print(y)
