# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:17:58 2022

@author: disrct
"""

class Casa():
    def __init__(self, janelas, portas, numLugares, proprietario = None):
        self._janelas = janelas
        self._portas = portas
        self._numLugares = numLugares
        self._proprietario = proprietario
        
    def fechaJanela(self):
        self._janelas = 'manual'
    
    def abreJanela(self):
        self._janelas = 'manual' 
        
    def trancaPortas(self):
        self._portas = 'automatico'
        
    def destrancaPortas(self):
        self._portas = 'automatico'
        
    def mostraDono(self):
        if self._proprietario == None:
            proprietario = 'Não há proprietario'
        else:
            proprietario = self._proprietario
            print(proprietario)
        
    
class Carro():
    def __init__(self, cor, potencia, placa, habilitacao):
        self._cor = cor
        self._potencia = potencia
        self._placa = placa
        self._habilitacao = habilitacao
        
    def habilitacaoNecessaria():
        Carro.habilitacao = 'categoria E'
    
class MotorHome(Casa,Carro):
    def __init__(self, janelas, portas, numLugares, proprietario, cor, potencia, placa, habilitacao):
        Casa.__init__(self, janelas, portas, numLugares, proprietario)
        Carro.__init__(self, cor, potencia, placa, habilitacao)
        
primeiroMotorHome = MotorHome("3", "2", "5", "Carlos", "Verde", "300cv", "ABD-3654", "")

primeiroMotorHome.imprimeEspecificacoes()
        
        
        
        
        
        
        
        
        
        
        
    