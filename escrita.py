# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:10:37 2022

@author: DISRCT
"""
import cv2
import numpy as np
#criando uma imagem de 512x512
img = np.zeros((512, 512, 3), np.uint8)

txt = 'Tabuleiro maneiro'

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, txt, (50,500), font, 1.5, (191,0,191), 4, cv2.LINE_AA)



cv2.imshow("tic-tac-toe", img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()