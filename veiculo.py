# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 08:58:08 2022

@author: disrct
"""

class Carro():
    def __init__(self, marca, cor, ano, proprietario=None):
        self._marca = marca
        self._cor = cor
        self._ano = ano
        self._proprietario = proprietario
        
    def ligar_carro(self):
        self._carro_ligado = "carro ligado"
    
    def desligar_carro(self):
        self._carro_ligado = "carro desligado"
    
    @staticmethod
    def transito_andando():
        Carro.transito = "andando sem transito"
    @staticmethod  
    def transito_parado():
        Carro.transito = "parado no transito"
            
    def mostrar(self):
        if self._proprietario == None:
            proprietario = 'Alguém'
        else:
            proprietario = self._proprietario
            print("\n{} está com o {}, seu veículo é: {} cor {}, ano {} e está {}".format(proprietario, self._carro_ligado, self._marca, self._cor, self._ano, Carro.transito))
            
            
carroCarla = Carro('Volkswagen', 'azul', 2008, 'Carla')
carroAna = Carro('Chevrolett', 'prata', 2016, 'Ana')

carroCarla.desligar_carro()
carroCarla.transito_parado()
carroCarla.mostrar()

carroAna.ligar_carro()
carroAna.transito_andando()
carroAna.mostrar()