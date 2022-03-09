# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 11:04:51 2022

@author: DISRCT
"""

def converte(dna):
    rna = ''
    complemento = {"A":"U", "G":"C", "C":"G", "T":"A"}
    
    for i in dna:
        rna = rna + complemento[i]
    return rna
    
dnaUsuario = str(input("Digite o DNA: "))

dnaUsuario = dnaUsuario.upper()

novoComplemento = converte(dnaUsuario)

print("A cadeia de RNA complementar é:", novoComplemento)


