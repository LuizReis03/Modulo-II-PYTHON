# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 10:04:01 2022

@author: DISRCT
"""

import cv2

image = cv2.imread("sunset.jpg", cv2.THRESH_BINARY)
image = cv2.resize(image, dsize=(750, 560), interpolation=cv2.INTER_CUBIC)
ret, image = cv2.threshold(image, 30, 500, cv2.THRESH_BINARY)

cv2.imshow("Binário", image)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()