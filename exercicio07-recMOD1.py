# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:05:09 2022

@author: DISRCT
"""

#---------------PROVA---------------
#---------------EXERCÍCIO 07---------------
alfabeto = {'a': 0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9,
            'k':10, 'l':11, 'm':12, 'n':13, 'o':14,
            'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21,
            'w':22, 'x':23, 'y':24, 'z':25}

def criptografia(x):
    print(x)
    global alfabeto
    for i in alfabeto:
        cont = i
        nova = alfabeto[i]
        for j in x:
            if j == cont:
                print(nova)
    
palavra = input("Digite a palavra para criptografar: ")
criptografia(palavra)