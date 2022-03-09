# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:33:22 2022

@author: DISRCT
"""
'''
#FILTRO BLUR
import cv2
image = cv2.imread("ruido.jpg")

 #passa os parâmetros do filtro
blur = cv2.blur(image,(5,5))

cv2.imshow("Filtrada", blur) #imagem filtrada
cv2.imshow("Original", image) #imagem original

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

'''

'''
#FILTRO GAUSSIANO
import cv2
image = cv2.imread("ruido.jpg")

 #passa os parâmetros do filtro
blur = cv2.GaussianBlur(image,(7,7), 0)

cv2.imshow("Filtrada", blur) #imagem filtrada
cv2.imshow("Original", image) #imagem original

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
'''

'''
#FILTRO SAL PIMENTA
import cv2
image = cv2.imread("ruido.jpg")

 #passa os parâmetros do filtro
median = cv2.medianBlur(image, 3)

cv2.imshow("Filtrada", median) #imagem filtrada
cv2.imshow("Original", image) #imagem original

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
'''