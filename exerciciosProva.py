# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 08:24:22 2022

@author: DISRCT
"""

#---------------------PROVA MODULO 2---------------------
#----------------------EXERCÍCIO 01----------------------
'''
import numpy as np
import random as rd

array = np.random.randint(50, size=(4, 4))
print("Array alearório")
print(array)
             
par = (array % 2 == 0)
array[par] = 0

print("\nArray com 0")
print(array)
'''

'''
#----------------------EXERCÍCIO 02----------------------
import pandas as pd
df = pd.read_csv('dados.csv', encoding='latin-1')
df = df.sort_values(by="preco") 
df = df.loc[df['bairro'] == 'Tijuca']
df = df.loc[df['quartos'] == 3]
df = df.loc[df['area'] > 130]
df = df.head(1)

print(df)
'''

#----------------------EXERCÍCIO 03----------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('gols_pr.csv', usecols=("clube", "gols_pro", "ano"))

x = df['ano'].unique()
y = df['gols_pro']

coxa = df.loc[df['clube'] == 'coritiba']
yc = coxa['gols_pro']
athletico = df.loc[df['clube'] == 'athletico-pr']
ya = athletico['gols_pro']
parana = df.loc[df['clube'] == 'parana']
yp = parana['gols_pro']
print(coxa, athletico, parana)

plt.plot(x, yc, color = 'g', label = 'Coritiba', linestyle = '-', marker = 'o', linewidth=3)
plt.plot(x, ya, color = 'r', label = 'Athletico-PR', linestyle = '-', marker = 'o', linewidth=3)
plt.plot(x, yp, color = 'b', label = 'Paraná', linestyle = '-', marker = 'o', linewidth=3)

plt.xticks([2010,2011,2012,2013,2014,2015,2016,2017,2018, 2019])
plt.yticks([30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140])
plt.xlabel('Gols')
plt.ylabel('Ano')
plt.legend()
plt.show()



#----------------------EXERCÍCIO 04----------------------
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, num=100, endpoint = True)
gf1 = x**2
gf2 = x**3

fig, eixo = plt.subplots(nrows=1, ncols = 2)

plt.grid(linestyle='-', linewidth=1)

eixo[0].plot(x, gf1, color='b')
eixo[1].plot(x, gf2, color='r')

plt.show()

'''

#----------------------EXERCÍCIO 05----------------------
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('flights.csv', sep=',')
df = df.loc[df['year'] == 1950]
print(df)

sns.catplot(y="month", x="passengers", kind="bar", palette="Set1", data=df);

'''

#----------------------EXERCÍCIO 06----------------------
'''
import cv2

image = cv2.imread("mulher.png")

#filtro
efeito = cv2.medianBlur(image,3)

cv2.imshow("Sal e Pimenta", efeito)
cv2.imshow("Original", image)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
'''

#----------------------EXERCÍCIO 07----------------------
'''
import cv2

cap = cv2.VideoCapture('flor.mp4')
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
output = cv2.VideoWriter("nova_flor.mp4", fourcc, 30.0, (1280,720))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame = cv2.flip(frame,1)
        output.write(frame)
        
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
cap.release()
output.release()
cv2.destroyAllWindows()

'''
#----------------------EXERCÍCIO 08----------------------

import os
import json
import time


def pegar_extensao(nome):
    index = nome.rfind('.')
    return nome[index:]


def organizar(diretorio):
    AUDIOS_DIR = os.path.join(diretorio, "audios")
    IMAGENS_DIR = os.path.join(diretorio, "imagens")
    DOCS_DIR = os.path.join(diretorio, "documentos")
    VIDEOS_DIR = os.path.join(diretorio, "videos")
    OUTROS_DIR = os.path.join(diretorio, "outros")
    
    if not os.path.isdir(AUDIOS_DIR):
        os.mkdir(AUDIOS_DIR)
    if not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)
        
    nomes_arquivos = os.listdir(diretorio)
    
    audios_ext = [".mp3", ".wav"]
    videos_ext = [".mp4", ".mov", ".avi"]
    docs_ext = [".txt", ".log", ".pdf"]
    imagens_ext = [".png", ".jpeg", ".jpg", ".jfif"]
    
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            extensao = str.lower(pegar_extensao(arquivo))
            print(arquivo, extensao)
            if extensao in audios_ext:
                nova_pasta = AUDIOS_DIR
            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR
            elif extensao in imagens_ext:
                nova_pasta = IMAGENS_DIR
            elif extensao in docs_ext:
                nova_pasta = DOCS_DIR
            else:
                nova_pasta = OUTROS_DIR
                
            tempo = time.time()
            formatTempo = time.ctime(tempo)
            print(time.ctime(tempo))

            velho = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)
            os.rename(velho, novo)
            d1 = {"Caminho antigo": velho, "Caminho novo:": novo, "timeStamp": formatTempo}
            s1 = json.dumps(d1)
            d2 = json.loads(s1)
            print(d2)
            
if __name__ == '__main__':
    organizar('pasta08')
