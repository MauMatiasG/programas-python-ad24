# Funcion con parametros que regresa un valor 
import os

def suma(n1, n2):
    s = n1 + n2
    return s

#Principal
os.system("cls")

#Caso 1 - el resultado se guarda en una variable
r = suma(100,200)
print("El resultado es ", r)

#Caso 2 - el resultado se calculo y se imprime directamente
print("\nOtra suma ", suma(500,200))

#Caso 3 - el usuario proporciona el valor de los parametros
print("\nDame dos numeros a sumar separados por <enter> ")
a , b = int(input()), int(input())
print("\nLa suma del usuario es ", suma(a, b))


