# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 08:05:51 2022

@author: disrct
"""

class Casa():
    def __init__(self, area, rua, cor, nome=None):
        self._nome = nome
        self._area = area
        self._rua = rua
        self._cor = cor
    def mostrar(self):
        if self._nome is None:
            nome = 'Alguém'
        else:
            nome = self._nome
        print("{} tem uma casa {} de {}m² na rua {}".format(nome, self._cor, self._area, self._rua))

    
casaPedro = Casa(240, 'Paula gomes', 'azul', 'Luiz')
casaJoao = Casa(650, 'José Loureiro', 'verde', 'Kleber')

casaJoao.mostrar()
casaPedro.mostrar()
