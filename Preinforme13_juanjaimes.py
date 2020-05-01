# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:22:07 2020

@author: JuanJaimes
"""
#----------------creacion del diccionario-------------------------#
#demanda de petroleo anual 2006-2020
#datos a partir de demanda en millones de dolares por dia
Petro_year={2006:85.3,
            2007:86.3,
            2008:85.8,
            2009:84.3,
            2010:86.4,
            2011:89,
            2012:89.8,
            2013:91.8,
            2014:92.7,
            2015:94.9,
            2016:96.2,
            2017:97.9,
            2018:99.3,
            2019:100.3,
            2020:101.6}
#--------------------poblematicas y su solucion------------------#
#problema 1: promedio de consumo
def operan (Petro_year):
    #recorriendo el diccionario y creando una lista
    petro=[]   
    for i in range (2006,2021,1):
        petro.append(Petro_year[i])
    #desvacion estandar
    cuadrados2=[]
    for o in petro:
        k=(sum(petro))**2
        cuadrados2.append(k)
    desviacion2=(sum(cuadrados2)/(len(petro)-1))**0.5
    print("la desviacion estandar de el consumo de petroleo es: \n"+str(round(desviacion2,2)))
    #media
    print("el promedio de consumo desde 2006 hasta 2020 es: "+str(round(sum(petro)/len(petro),2)))
    #mediana
    for recorrido in range (1,len(petro)):                      
        A=(petro[7]+petro[8])/2
        for posicion in range(len(petro)-recorrido):
            #metodo burbuja para organizar.
            if petro[posicion]>petro[posicion+1]:
                temp=petro[posicion]
                petro[posicion]=petro[posicion+1]
                petro[posicion+1]=temp
    print("la  mediana es: "+str(A))
    
    
def bonus (Petro_year):
    #mayor dato 
    petro2=[]
    for i in range (2006,2021,1):
        petro2.append(Petro_year[i])
        for recorrido in range (1,len(petro2)):
            for posicion in range(len(petro2)-recorrido):
            #encuentro el valor mas alto
                A=petro2[0]            
                for posicion in range(len(petro2)-recorrido):
                    #metodo burbuja para organizar.
                    if petro2[posicion]<petro2[posicion+1]:
                        temp=petro2[posicion]
                        petro2[posicion]=petro2[posicion+1]
                        petro2[posicion+1]=temp
    print("el mayor consumo de petroleo fue: "+str(A))
    petro3=[]
    for i in range (2006,2021,1):
        petro3.append(Petro_year[i])
        for recorrido in range (1,len(petro3)):
            for posicion in range(len(petro3)-recorrido):
            #encuentro el valor mas bajo
                B=petro3[0]            
                for posicion in range(len(petro3)-recorrido):
                    #metodo burbuja para organizar.
                    if petro3[posicion]>petro3[posicion+1]:
                        temp=petro3[posicion]
                        petro3[posicion]=petro3[posicion+1]
                        petro3[posicion+1]=temp
    print("el menor consumo de petroleo fue: "+str(B))
    
    
            
    
                          
    
    


#--------------------------------fin.---------------------------#
    #hecho por juan_jaimes & david sepulveda#
#llamo las funciones
operan(Petro_year)
bonus(Petro_year)
        

    
    
   
    

