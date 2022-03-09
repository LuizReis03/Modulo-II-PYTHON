# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:02:33 2022

@author: DISRCT
"""

import cv2
import numpy as np

image = cv2.imread("Flor.png", 0)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(image,kernel,iterations=1)

cv2.imshow("Erosão", erosion)
cv2.imshow("Original", image)

cv2.waitKey(0)
cv2.destroyAllWindows()