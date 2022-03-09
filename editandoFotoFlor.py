# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:52:35 2022

@author: DISRCT
"""

import cv2

image = cv2.imread("Flor.png")

#filtro
salPiment = cv2.medianBlur(image, 9)

cv2.imshow("Sal e Pimenta", salPiment)
cv2.imshow("Original", image)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()