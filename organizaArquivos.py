# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:45:23 2022

@author: DISRCT
"""

import os
from datetime import datetime


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
                
            data = datetime.now()
            velho = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)
            os.rename(velho, novo)
            print("Moveu:",velho,"->", novo, "-> Horário de tranferência:", data.strftime("%H:%M:%S.%f"))
            
if __name__ == '__main__':
    organizar('pastaExercicio')

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            