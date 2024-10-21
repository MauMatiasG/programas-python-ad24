# Funcion con parametros

import os

def saluda(nombre):
    print(f"Hola -{nombre} bienvenido a Python, tu nombre tiene {len(nombre)} caracteres")

#Programa principal
os.system("cls")
saluda("Carlos Castaneda")
saluda("Juan Perez Diaz")
saluda("Maria Soto Garcia")
saluda(20)