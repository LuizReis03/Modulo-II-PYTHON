# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:02:49 2022

@author: disrct
"""

class InstrumentoEscrita:
    def __init__(self, material):
        self._material = material
        
    def escrever(self):
        print("Escrevendo...")
    
    def desenhar(self):
        print("Desenhando...")
    
    def pintar(self):
        print("Pintando...")
        
class lapis(InstrumentoEscrita):
    def __init__(self, grafite_n = 0.7):
        super().__init__("Grafite")
        self._grafite = grafite_n
        
lapisLuiz = lapis(75.5)
print(lapisLuiz._material)
lapis.pintar(lapisLuiz)