# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:21:30 2022

@author: DISRCT
"""

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.circle(img,(75,75),40,(191,0,191), -1)

cv2.ellipse(img, (420, 450), (60, 20), 0, 0, 360, (500, 150, 150), -1)

cv2.rectangle(img, (200,200), (300,300), (0,0,255), -1)


cv2.imshow("figuras-geometricas", img)
x = cv2.waitKey()
cv2.destroyAllWindows()

img2 = np.zeros((512, 512, 3), np.uint8)
cv2.putText(img2, str(x), (210,256), font, 1.5, (191,0,191), 4, cv2.LINE_AA)
cv2.imshow("imagem 2", img2)
cv2.waitKey(1000)
cv2.destroyAllWindows()