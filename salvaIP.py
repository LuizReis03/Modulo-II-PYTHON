# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 08:33:51 2022

@author: disrct
"""

def ipv4(ip):
    ip1 = ip.split('.')
    if len(ip1) != 4:
        print("Endereço inválido")
        arquivo = open('IPs_invalidos.txt', 'a')
        arquivo.write('IP: {}\n'.format(ip))
        arquivo.close()
        return False
    else:
        for num in ip1:
            if num.isdigit() == False:
                print("Endereço invalido")
                arquivo = open('IPs_invalidos.txt', 'a')
                arquivo.write('IP: {}\n'.format(ip))
                arquivo.close()
                return False
            else:
                if int(num) > 255 or int(num) < 0:
                    print("Endereço inválido")
                    arquivo = open('IPs_invalidos.txt', 'a')
                    arquivo.write('IP: {}\n'.format(ip))
                    arquivo.close()
                    return False         
    print("Endereço válido")
    arquivo = open('IPs_validos.txt', 'a')
    arquivo.write('IP: {}\n'.format(ip))
    arquivo.close()
    
ip = (input("Inisira um endereço de IP: "))
print('O endereço de ip: {} é {}.'.format(ip, ipv4(ip)))