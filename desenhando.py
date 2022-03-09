# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 08:51:08 2022

@author: DISRCT
"""

import cv2
import numpy as np
#criando uma imagem de 512x512
img = np.zeros((512, 512, 3), np.uint8)

txt = 'Jogo da velha'

font = cv2.FONT_HERSHEY_SIMPLEX

# linhas horizontais
cv2.line(img, (150,0), (150, 512), (255,255,255), 5)
cv2.line(img, (350,0), (350, 512), (255,255,255), 5)

# linhas verticais
cv2.line(img, (0,150), (512, 150), (255,255,255), 5)
cv2.line(img, (0,350), (512,350), (255,255,255), 5)

#criando um retangulo (imagem, (passa cordenada), (cor))
cv2.rectangle(img, (200,200), (300,300), (0,255,0), -1)

#circulo (imagem, (cordenada), raio, cor, thickness)
cv2. circle(img,(75,75),50,(0,0,255), -1)

#escrita
cv2.putText(img, txt, (10,500), font, 0.7, (191,0,191), 4, cv2.LINE_AA)

cv2.imshow("tic-tac-toe", img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()