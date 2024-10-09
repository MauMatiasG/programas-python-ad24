# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

import os; os.system("cls")

cadena = input("Escribe una cadena: ")

contador = {}

for caracter in cadena:
    if caracter in contador:
            contador[caracter] += 1
    else:
            contador[caracter] = 1
            
print(contador)

