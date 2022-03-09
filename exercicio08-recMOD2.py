# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 10:49:11 2022

@author: DISRCT
"""

import json
import time
import os

antigo = 'S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Luiz Henrique Gomes dos Reis/modulo2/provaRecModulo2/pasta_antiga'
novo = 'nova_pasta'
nome_arquivos = os.listdir(antigo)

for arquivo in nome_arquivos:
    if os.path.isdir(novo) == False:
        os.mkdir('nova_pasta')
    else:
        caminho_antigo = os.path.join(antigo,arquivo)
        caminho_novo = os.path.join(novo, arquivo)
        os.rename(caminho_antigo, caminho_novo)
        saida = {'caminho antigo': caminho_antigo, 'caminho novo': caminho_novo, 
                 'timeStamp': time.ctime()}
        saida = json.dumps(saida)
        print(saida)
