# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 08:15:08 2022

@author: DISRCT
"""

import os

diretorio = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Luiz Henrique Gomes dos Reis/modulos/modulo2/modulo OS/pastaExercicio"
novo_local = os.path.join(diretorio, 'nova_pasta')
os.mkdir(novo_local)
print(novo_local)

arquivo = "gaviao.jpg"

velho = os.path.join(diretorio, arquivo)
novo = os.path.join(novo_local, arquivo)
os.rename(velho, novo)