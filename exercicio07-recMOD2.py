# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 10:14:33 2022

@author: DISRCT
"""

import cv2

cap = cv2.VideoCapture('flor.mp4')
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
output = cv2.VideoWriter("flor_editado.mp4", fourcc, 30.0, (1280,720))
print("EFEITOS:\n 1 - Preto e branco \n 2 - HSV \n 3 - RGB \n")
escolha = int(input("Digite o efeito que deseja: "))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        try:
            if escolha == 1:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                output.write(frame)
                cv2.imshow('frame', frame)
            elif escolha == 2: 
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                output.write(frame)
                cv2.imshow('frame', frame)
            elif escolha == 3:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                output.write(frame)
                cv2.imshow('frame', frame)
            elif escolha != 1 and escolha != 2 and escolha != 3:
                print("Só é aceito numeros de 1 a 3")
                break
        except:
            print("Verifique o que foi digitado")
            break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
cap.release()
output.release()
cv2.destroyAllWindows()