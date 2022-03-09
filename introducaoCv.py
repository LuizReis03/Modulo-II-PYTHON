# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 08:15:09 2022

@author: DISRCT
"""

import cv2
import numpy as np

gaviao = cv2.imread('gaviao.jpg', cv2.IMREAD_COLOR)
gaviao2 = cv2.imread('gaviao.jpg', cv2.IMREAD_GRAYSCALE)
gaviao3 = cv2.imread('gaviao.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('gaviao1', gaviao)
cv2.imshow('gaviao2', gaviao2)
cv2.imshow('gaviao3', gaviao3)
cv2.waitKey(0)
x = cv2.waitKey(0)
print('TECLA APERTADA:', x)
cv2.destroyAllWindows()
