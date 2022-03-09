# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:54:43 2022

@author: DISRCT
"""
#---------------PROVA---------------
#---------------EXERCÍCIO 04---------------
lista = []
media = 0.0

nome = input("Digite o nome do aluno: ")

qtdeProvas = int(input("Digite a quantidade de provas: "))

for i in range(qtdeProvas):
    notaProva = float(input("Qual a nota da {}º prova: ".format(i+1)))
    lista.append(notaProva)

media = sum(lista) / qtdeProvas
    
aluno = {'Nome': nome, 'Notas': lista, 'Média': media}
print(aluno)
