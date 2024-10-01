# Leer un número de mes (ej 4).
# Imprimir: días del mes, y nombre del mes (ej marzo, 30).
# Asume 28 para febrero, guarda días en una lista, y nombres de mes en otra.

import os; os.system("cls")

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    nm = int(input("Numero de mes (1-12) ? "))
    if nm>=1 and nm<=12:
        print(f"\n{meses[nm-1]}, {dias[nm-1]}")
        break
    else:
        print("Ingresa un numero de mes del 1 a 12")