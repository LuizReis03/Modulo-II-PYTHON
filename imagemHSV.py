# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:26:33 2022

@author: DISRCT
"""

import cv2
img = cv2.imread("gaviao.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("panda_hsv", img_hsv)
cv2.imshow("original", img)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()