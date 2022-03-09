# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:42:57 2022

@author: DISRCT
"""

import time

tempo = time.time()
print(time.ctime(tempo))


secondsSinceEpoch = time.time()
timeObj = time.localtime(secondsSinceEpoch)