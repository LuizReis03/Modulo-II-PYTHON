# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:57:45 2022

@author: DISRCT
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 08:17:49 2022

@author: DISRCT
"""
#---------------------CONVERSÃO---------------------
'''
celsius = float(input("Digite a temperatura em Celsiu7s: "))

farhent = (9*celsius)/5 + 32

print("A temperatura {} em Farenheint é: {}".format(celsius, farhent))
'''

#---------------------3 primeiras maiusculas---------------------
'''
nome = input("Digite seu nome: ")

print(nome[:3].upper())
'''

#---------------------3 primeiras maiusculas---------------------
'''
nome = input("Digite seu nome completo em letras minusculas: ")
maiusculas = nome.title()
print(maiusculas)
maiusculas = maiusculas.split(' ')
tamanho = 0

for i in maiusculas:
   t = len(i)
   tamanho += t

print("Seu nome possui {} caracteres".format(tamanho))
'''

#---------------------Lista ordenada---------------------
'''
lista = []
for i in range(10):
    ajuste = i + 1
    numUsuario = int(input("VALOR {}: ".format(ajuste)))
    lista.append(numUsuario)
    lista.sort()
    
print("\nTAMANHO DA LISTA:", len(lista))
print(lista)
'''

#---------------------Tupla dos mais ricos---------------------
'''
maisRicos = ('Jeff Bezos', 'Bill Gates', 'Warren Buffet', 'Bernard Arnault', 'Amância Ortega',
             'Larry Ellsion', 'Mark Zuckerberg', 'Miche. Bloomberg', 'Larry Page')

print("\nOs 10 mais ricos do mundo são:", maisRicos)
print("\nOs 3 mais ricos do mundo são:", maisRicos[:3])
print("\nO mais rico do mundo é:", maisRicos[0])
'''

#---------------------Dicionário de Cardapio---------------------
'''
menu = {'Hamburguer': 10, 'Hotdog': 6.5, 'Salada': 4,
        'Suco': 4, 'Refrigerante': 4.5, 'Água': 2}

print("-------------------CARDÁPIO-------------------")
print("\n",menu)

  
comida = input("Digite a comida deseja: ")
bebida =  input("Digite a bebida deseja: ")
soma = menu[bebida] + menu[comida]

print("O valor total é: R${}".format(soma))
'''

#---------------------Número secreto---------------------
'''
import random
numeroSecreto = random.randint(0,10)
print("JOGO DA ADIVINHAÇÃO \n--------------------------")
print("\nO NÚMERO SECRETO VAI DE 1 A 10 - VOCÊ TEM 3 CHANCES")
chances = 3
while True:
    try:
        numUsuario = int(input("Digite um número: "))
        chances = chances - 1
        if chances == 0:
            print("Suas chances acabaram! :( ")
            break
        elif numUsuario == numeroSecreto:
            print("Parabens você acertou! O número secreto é {}".format(numeroSecreto))
            break
        elif numUsuario != numeroSecreto:
            print("Não é esse o número secreto!")
            continue
    except:
        print("Verifique o que foi digitado!")

'''

#---------------------Voto usuário---------------------
'''
anoUsuario = int(input("Qual ano você nasceu? "))
ano = 2022
verifica = ano - anoUsuario 

if verifica > 0 and verifica <= 16:
    print("Não é permitido votar!")
elif verifica > 16 and verifica < 18:
    print("Seu voto é facultativo!")
elif verifica >= 18 and verifica <= 70:
    print("Seu voto é obrigatório!")
elif verifica > 70:
    print("Seu voto é facultativo!")
'''

#---------------------Soma de numeros naturais---------------------
'''
limite = int(input("Digite qual o limite para a soma: "))
lista = []

for i in range(limite):
    i+=1
    lista.append(i)
    
print("O valor total da soma é:", sum(lista))
'''

#---------------------Calculadora---------------------
'''
while True:
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        operacao = int(input("Digite: \n1-Soma \n2-Subtração \n3-Multiplicação \n4-Divisao \n"))
        if operacao == 1:
            soma = num1 + num2
            print("\nO resultado é:",soma)
        elif operacao == 2:
            subt = num1 - num2
            print("\nO resultado é:",subt)
        elif operacao == 3:
            mult = num1 * num2
            print("\nO resultado é:",mult)
        elif operacao == 4:
            div = num1 / num2
            print("\nO resultado é:",div)
            
        sair = input("Deseja sair? (s/n)")
        if sair == 's':
            break
        elif sair == 'n':
            continue
        else:
            print("Verifique o que foi digitado")
            break
    except:
        print("Verifique o que foi digitado")

'''

#---------------------Números pares---------------------
'''
for i in range(31):
    if i % 2 == 0:
        print(i)
'''

#---------------------Números pares---------------------
'''
numUsuario = int(input("Digite um número: "))

for i in range(numUsuario):
    for j in range(numUsuario):
        print("x", end = " ")
    print("\n", end = " ")
'''

#---------------------Fibonacci---------------------
'''
fatores = int(input("Digite o número de fatores: "))

num1 = 0
num2 = 1
num3 = num1 + num2

for i in range(fatores):
    print(num1)
    num3 = num1 + num2
    num1 = num2
    num2 = num3
''' 
    
#---------------------Numeros primos---------------------
'''
primo = int(input("Digite um numero: "))

if primo == 2 or primo == 3 or primo == 5:
    print("É primo")
elif primo % 2 != 0 and primo % 3 != 0 and primo % 5 != 0:
    print("É primo")
else:
    print("Não é primo")
'''

#---------------------Função Palídromos---------------------
'''
def verificaPalavra(x):
    x = x.replace(" ","")
    invertido = x[::-1]
    
    if invertido == x:
        print("{} É UM PALIDROMO". format(x.lower()))
    else:
        print("{} NÃO É UM PALIDROMO". format(x.lower()))

    
palavra = str(input("Digite uma palavra para verificar se é palídromo ou não: "))
verificaPalavra(palavra)
'''



