#Funcion que calcula el mayor de 3 numeros

import os

def mayor(n1, n2, n3):
    may = -1
    if n1>n2 and n1>n3:
        may = n1
    if n2>n1 and n2>n3:
        may = n2
    if n3>n1 and n3>n2:
        may = n3
    return may

#Principal
os.system("cls")
n1 = int(input("DNumero 1 : "))
n2 = int(input("DNumero 2 : "))
n3 = int(input("DNumero 3 : "))
r = mayor (n1, n2 ,n3)

if r != -1:
    print("El mayor es ", r) 
else:
    print("Los numeros son iguales o hay dos iguales, por lo tanto no hya uno que sea el mayor")   