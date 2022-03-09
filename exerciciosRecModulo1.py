# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 08:10:58 2022

@author: DISRCT
"""

#----------------Exercício 01----------------
'''
#FUNÇÃO PARA SUBSTITUIR NA PALAVRA O PRIMEIRO CACTERE PELO SEGUNDO
def sub_caractere(palavra, c1, c2):
    palavra = palavra.replace(c2, c1)
    print(palavra)

palavraUser = input("Digite uma palavra: ")
c1 = input("Digite uma letra: ")
c2 = input("Digite mais uma letra: ")
sub_caractere(palavraUser, c1, c2)
'''

#----------------Exercício 02----------------
'''
def decompoeNumero(x):
    valor = x
    
    for i in valor:
        notas100 = valor % 100
        
    print(notas100)
            
    
numUsuario = float(input("Digite um valor com duas casas decimais: "))
decompoeNumero(numUsuario)

'''

#----------------Exercício 03----------------
'''
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

#primeiro quadrante os dois sao positivos
#segundo quadrante o x é negativo e o y positivo
#terceiro ambos sao negativos
#quarto x é positivo e y negativo

while True:
    try:
        if x == 0 and y == 0:
            print("\nA coordenada {},{} está na origem".format(x,y))
            break
        elif x > 0 and y > 0:
            print("\nA coordenada {},{} está no primeiro quadrante".format(x,y))
            break
        elif x < 0 and y > 0:
            print("\nA coordenada {},{} está no segundo quadrante".format(x,y))
            break
        elif x < 0 and y < 0:
            print("\nA coordenada {},{} está no terceiro quadrante".format(x,y))
            break
        elif x > 0 and y < 0:
            print("\nA coordenada {},{} está no quarto quadrante".format(x,y))
            break
    except:
        print("znVerifique o que foi inserido... digite novamente")
'''

#----------------Exercício 04----------------
'''
listaPar = []
listaImpar = []

for i in range(15):
    try:
        numAleatorio = int(input("Digite o valor {}: ".format(i+1)))
        if numAleatorio % 2 == 0:
            listaPar.append(numAleatorio)
        else:
            listaImpar.append(numAleatorio)
        if len(listaPar) == 5:
            print("ENCHEU A LISTA PAR:", listaPar)
            listaPar.clear()
            print("RESET lista:", listaPar)
        elif len(listaImpar) == 5:
            print("ENCHEU A LISTA IMPAR:", listaImpar)
            listaImpar.clear()
            print("RESET lista:", listaImpar)
    except:
        print("Verifique o que foi inserido...")
        
print("\n---RESTO DAS LISTAS---")
print("Lista par:", listaPar)
print("Lista impar:", listaImpar)
'''

#----------------Exercício 05----------------
'''
import operator
liga = {'Corinthians': 0, 'Palmeiras': 0, 'Gremio': 0, 'Santos': 0}

#VERIFICA PLACAR CORINTHIANS
for i in range(3):
    placarCorinthians = input("Qual foi o resultado do Corinthians na {}º rodada: ". format(i+1))
    if placarCorinthians == 'V' or placarCorinthians == 'v':
        liga['Corinthians'] = liga['Corinthians'] + 3
    if placarCorinthians == 'E':
        liga['Corinthians'] = liga['Corinthians'] + 1
    if placarCorinthians == 'D':
        liga['Corinthians'] = liga['Corinthians'] + 0
        
        
#VERIFICA PLACAR PALMEIRAS
for i in range(3):
    placarPalmeiras = input("Qual foi o resultado do Palmeiras na {}º rodada: ". format(i+1))
    if placarPalmeiras == 'V' or placarPalmeiras == 'v':
        liga['Palmeiras'] = liga['Palmeiras'] + 3
    if placarPalmeiras == 'E':
        liga['Palmeiras'] = liga['Palmeiras'] + 1
    if placarPalmeiras == 'D':
        liga['Palmeiras'] = liga['Palmeiras'] + 0   
        
        
#VERIFICA PLACAR GREMIO

for i in range(3):
    placarGremio = input("Qual foi o resultado do Gremio na {}º rodada: ". format(i+1))
    if placarGremio == 'V' or placarGremio == 'V':
        liga['Gremio'] = liga['Gremio'] + 3
    if placarGremio == 'E':
        liga['Gremio'] = liga['Gremio'] + 1
    if placarGremio == 'D':
        liga['Gremio'] = liga['Gremio'] + 0
        
        
#VERIFICA PLACAR SANTOS
for i in range(3):
    placarSantos = input("Qual foi o resultado do Santos na {}º rodada: ". format(i+1))
    if placarSantos == 'V' or placarSantos == 'v':
        liga['Santos'] = liga['Santos'] + 3
    if placarSantos == 'E':
        liga['Santos'] = liga['Santos'] + 1
    if placarSantos == 'D':
        liga['Santos'] = liga['Santos'] + 0


#VERIFICA MAIOR SOMADOR E MENOR SOMADOR
maior = max(liga, key=lambda key: liga[key])
menor = min(liga, key=lambda key: liga[key])
        
print("O maior pontuador foi:", maior)
print("O menor pontuador foi:", menor)
'''
'''
#----------------Exercício 06----------------
def ajustaHorario(hora):
    horaConvert = int(hora)
    print(horaConvert)
    

print("EX: 15:30 / 08:30")
entrada = input("Digite o horário conforme o exemplo acima: ").split(':', 1)
ajustaHorario(entrada)
'''






