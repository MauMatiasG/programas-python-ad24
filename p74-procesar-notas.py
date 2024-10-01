# Leer n notas hasta introducir un 0. Las notas pueden estar entre 0 y 100 (validar)
# Imprime:
#   ◦ cuantas notas, las notas,
#   ◦ suma, promedio,
#   ◦ notas menores al promedio y cuantas son
#   ◦ nota máxima y nota mínima

import os; os.system("cls")

n = ""
suma = promedio = 0
nums = []

while n!= 0:
    n = float(input("Nota: "))
    if n>0 and n<=100:
        nums.append(n)
    elif 0>n:
        print("Escribe una nota entre 0 y 100")
    elif n>100:
        print("Escribe una nota entre 0 y 100")

print("< fin")

for n in nums:
    suma += n
promedio = suma / len(nums)

mp=[]
for n in nums:
    if n < promedio:
        mp.append(n)

print()
print("Cuantas notas son                     :", len(nums))
print("Las notas son                         :", nums)
print("La suma es                            :", suma)
print("El promedio es                        :", promedio)
print("Menores al promedio                   :", mp)
print("Cuantas son menores al promedio       :", len(mp))
print("Mayor y Menor                         :", max(nums), min(nums))

