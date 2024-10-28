# Función que pida 3 números enteros y devuelva el menor de ellos, usando una función
import os

def menor(n1, n2, n3):
    may = -1
    if n1<n2 and n1<n3:
        may = n1
    if n2<n1 and n2<n3:
        may = n2
    if n3<n1 and n3<n2:
        may = n3
    return may

#Principal
os.system("cls")
n1 = int(input("Numero 1 : "))
n2 = int(input("Numero 2 : "))
n3 = int(input("Numero 3 : "))
r = menor (n1, n2 ,n3)

if r != -1:
    print("El menor es ", r) 
else:
    print("Los numeros son iguales o hay dos iguales, por lo tanto no hya uno que sea el mayor")   