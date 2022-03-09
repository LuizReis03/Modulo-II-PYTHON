# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:18:40 2022

@author: DISRCT
"""

#---------------PROVA---------------
#---------------EXERCÍCIO 05---------------
meses = {'01':'Janeiro', '02':'Fevereiro', '03':'Março', '04':'Abril',
         '05':'Maio', '06':'Junho', '07':'Julho', '08':'Agosto',
         '09':'Setembro', '10': 'Outubro', '11': 'Novembro', '12':'Dezembro'}

data = input("Digite a data atual (ex: 01/04/2022): ")
lista = data.split('/')
dia, mes, ano = data.split('/')    
convertDia = int(dia)
novo_mes = meses[mes]

convertMes = int(mes)
if convertMes < 0 or convertMes > 12:
    print("Foi digitado algo não aceito em DIA")
elif convertDia < 0 or convertDia > 31:
    print("Foi digitado algo não aceito em DIA")
else:
    print("{} de {} de {}".format(dia, novo_mes, ano))
