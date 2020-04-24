# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:52:40 2020

@author: DAVID LEONARDO
"""


import numpy as np



def imprimir ():
    print("Ingresos")
    for i in range(0,filas):
        print (ciudades[i],ingresos[i])
    print("Egresos")
    for i in range(0,filas):
        print (ciudades[i],egresos[i])
imprimir ()


p









def imprimir_personalizado(ingresos,minmes,maxmes):
    i_personalizado=ingresos[:4,minmes-1:maxmes]
    for i in range (0,filas):
        print(ciudades[i],i_personalizado[i])
    return i_personalizado
imprimir_personalizado(ingresos,3,6)