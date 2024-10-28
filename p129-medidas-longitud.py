# Programa con dos funciones que convierta: pulgadas a centímetros y metros a pies.
# Deberá́ mostrar un menú con las opciones correspondientes.

import os

def in_cm (n):    
    return n * 2.54

def mts_fts(n):
    return n * 3.281

#Principal
os.system("cls")
print('[ 1 ] Convertir Pulgadas a Centrimetros')
print('[ 2 ] Convertir Metros a Pies')

op = int(input("Elige ? "))

if op==1 :
    n = int(input('Dame una longitud en pulgadas? '))
    print(f'La longitud en centimetros es {in_cm(n):.3f}')
elif op==2:
    n = int(input('Dame una longitud en metros? '))
    print(f'La longitud en pies es {mts_fts(n):.3f}')