# Funcion que recibe dos parametros

import os

def saluda(apaterno, nombre):
    print(f"Hola {apaterno} {nombre} longitud {len(apaterno+nombre)}")

#Programa principal
os.system("cls")
saluda("Castaneda", "Carlos")
#saluda("Soto")
#saluda("Soto", "Bernal", "Rocio")