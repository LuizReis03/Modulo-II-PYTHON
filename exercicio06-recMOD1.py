# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:45:20 2022

@author: DISRCT
"""

#---------------PROVA---------------
#---------------EXERCÍCIO 06---------------

while True:
    try:
        valorProduto = float(input("Digite o valor do produto em dólares: "))
        estado = input("Digite para qual estado será transportado (MG,SP,RJ ou MS): ")
        estado.lower()
        dolar = 5.12
        if estado == 'mg':
            imposto = dolar * 0.07
            result = dolar + imposto
            print("Valor final é:", round(result,2))
            break
        elif estado == 'sp':
            imposto = dolar * 0.12
            result = dolar + imposto
            print("Valor final é:", round(result,2))
            break
        elif estado == 'rj':
            imposto = dolar * 0.15
            result = dolar + imposto
            print("Valor final é:", round(result,2))
            break
        elif estado == 'ms':
            imposto = dolar * 0.08
            result = dolar + imposto
            print("Valor final é:", round(result,2))
            break
    except:
        print("Verifique o que foi digitado...")
        break