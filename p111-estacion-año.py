#Funcion que regresa una cadena con la estacion del año, recibe como parametro un numero entre 1 y 4

import os

def estacion(n):
    if n==1:
        return "Primavera"
    elif n==2:
        return "Verano"
    elif n==3:
        return "Otoño"
    elif n==4:
        return "Invierno"
    else:
        return "Error"
    
#Principal
os.system("cls")
n = int(input("Dame la estacion del anño (1-4) y te la doy con letra: "))
print(f"La estacion es {estacion(n)}")
    