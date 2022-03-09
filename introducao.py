# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:35:49 2022

@author: DISRCT
"""

from datetime import datetime

data = datetime.now()
print(data.strftime("Dia: %d/%m/%y \nHora: %H:%M:%S.%f"))