# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:01:58 2020

@author: abaly
"""

#&& ejercicio 5

#aqui se ponen las entradas

a= int(input("ingrese el valor de a: "))
b= int(input("ingrese el valor de b: "))
d= int(input("ingrese el valor de d: "))

#aqui se realizan las operaciones y se imprimen

print("el doble de a es:"+ str(int(a*2)))
print("el residuo de la division es: "+ str(int(a%b)))
print("el cuadrado de b es: "+ str(int(b**2)))
print("la raiz cuadrada de d es: "+str(int(d**(1/2))))

#&& ejercicio 12
#aqui se ingresan las variables
a= int(input("ingrese a: "))
b= int(input("ingrese b: "))
c= int(input("ingrese c: "))
#aqui se aplica la formula 
d= (b**2)-(4*a*c)
#aqui usamos condicional para hallar las x
if d>0 :
    print("x1: "+str(((-b)+(d**(1/2))/(2*a))))
    print("x2: "+str(((-b)+(d**(1/2))/(2*a))))
elif d==0 :
    print("x1 y x2 son iguales, y su valor es: "+str((-b)/(2*a)))
elif d<0:
    print("i")
    
    
