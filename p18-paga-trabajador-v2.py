# Calcular la paga de un trabajador considerando las horas extras

import os; os.system("cls")

print("Calcular la paga de un trabajador considerando las horas extras\n")

nombre = input("Dame tu nombre ? ")
horas = int(input("Horas trabajadas ? "))
paga = float(input("Paga x hora ? "))

tasa = 0.03
hextra = paganormal = pagaextra = pagabruta = 0 

if horas > 40:
    hextra = horas - 40
    paganormal = 40 * paga
    pagaextra = hextra * paga * 2
    pagabruta = paganormal + pagaextra
else:
    pagabruta = horas * paga

impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print(f"\nEl trabajador {nombre}, trabajo {horas} horas, a una paga de {paga:.2f}")
print(f"\nHoras exra: {hextra}, Paga normal: {paganormal}, Paga extra: {pagaextra}")
print(f"Paga bruta       : {pagabruta:.2f}")
print(f"Impuesto         : {impuesto}")
print(f"Paga neta        : {paganeta:.2f}")
