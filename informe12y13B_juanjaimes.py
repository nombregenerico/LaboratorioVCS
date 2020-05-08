# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:50:47 2020

@author: alquimistaCore
"""
#libreria ramdom
from collections import Counter
from random import choice
#----parte b diccionarios#---#

#------ejercicio 11-------#
#diccionario
ponderado={"A":1,
           "2":2,
           "3":3,
           "4":4,
           "5":5,
           "6":6,
           "7":7,
           "8":8,
           "9":9,
           "J":10,
           "Q":10,
           "K":10,} 
#---------------ejericio 12----------------#
#lista
simbolos=["(C)","(D)","(T)","(P)"]

#--------------ejercicio 13------------#
#funcion para barajar
def combinar(ponderado,simbolos):
    baraja = {}
    for combi in ponderado:
        for sim in simbolos:
            baraja[combi+sim]=ponderado[combi]

    return baraja
#llamo la funcion para asiganrsela a baraja
baraja=combinar(ponderado,simbolos)

#-------------ejercicio 14----------------#
#generacion de diccionario aleatorio
def revolver(baraja):
  key_list = []
  values_list = []
  A=len(baraja)
  for i in range(A):
    key_list.append(choice(Counter(baraja).most_common(A))[0])
    values_list.append(baraja[key_list[i]])
  
  baraja.clear()
  for i in range(A):
    baraja[key_list[i]]=values_list[i]
  return baraja
baraja=revolver(baraja)
#----------------ejercicio 15---------------------------#
#barajas
cartas_jugador=[]
cartas_tallador=[]
#-----------------ejercicio 16--------------------------------#
def repartir(cartas, baraja):
    keys=[]
    for key in baraja:
        keys.append(key)

    if len(cartas) == 0:
        cartas.append(keys[0])
        del baraja[keys[0]]
        del keys[0]

        cartas.append(keys[0])
        del baraja[keys[0]]
        del keys[0]
    else:
        cartas.append(keys[0])
        del baraja[keys[0]]
        del keys[0]
    return cartas

cartas_jugador= repartir(cartas_jugador,baraja)
cartas_tallador= repartir(cartas_tallador,baraja)


            
