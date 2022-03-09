# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 09:52:53 2022

@author: disrct
"""

def calculaProdutos(arquivo):
    produtos = arquivo.read()
    organizaProdutos = produtos.split('\n')
    resultado = 0
    for i in organizaProdutos:
        peça, preco = i.split(": ")
        resultado = resultado + int(preco)
    print("A soma total é: R${}".format(resultado))
    
    
arquivo = open('Nome_e_preco.txt', 'r')
calculaProdutos(arquivo)
arquivo.close()