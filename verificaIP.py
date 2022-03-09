# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 08:28:50 2022

@author: disrct
"""

def ipv4(ip):
    ip1 = ip.split('.')
    if len(ip1) != 4:
        print("endereco invalido")
        return False
    else:
        for num in ip1:
            if num.isdigit() == False:
                print("endereco invalido")
                return False
            else:
                if int(num) > 255 or int(num) < 0:
                    print("Endereço inválido")
                    return False         
    print("Endereço válido")
    return True
    
ip = (input("Inisira um endereço de IP: "))
print('O endereço de ip: {} é {}.'.format(ip, ipv4(ip)))