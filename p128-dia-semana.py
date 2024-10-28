# Función que pida un número entero entre 1 y 7 y devuelva el día de la semana con letra.

import os

def dia(n):
    if n==1:
        return "Lunes"
    elif n==2:
        return "Martes"
    elif n==3:
        return "Miercoles"
    elif n==4:
        return "Jueves"
    elif n==5:
        return "Viernes"
    elif n==6:
        return "Sabado"
    elif n==7:
        return "Domingo"
    else:
        return "Error"
    
#Principal
os.system("cls")
n = int(input("Dame el dia de la semana (1-7) y te la doy con letra: "))
print(f"El dia es {dia(n)}")