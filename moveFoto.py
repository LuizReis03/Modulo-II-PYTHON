# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 10:35:55 2022

@author: DISRCT
"""

import os 
diretorio = "S:\COM\Human_Resources\01.Engineering_Tech_School\02.Internal\10 - Aprendizes\6 - Programador Web 2022\Luiz Henrique Gomes dos Reis\modulos\modulo2\exercicioRevisao\exercicio01"

novo_local = os.path.join(diretorio, 'Graficos')
os.mkdir(novo_local)
print(novo_local)

arquivo = 'graficoParOuImpar.png'
velho = os.path.join(diretorio, arquivo)
novo = os.path.join(novo_local, arquivo)
os.rename(velho, novo)