# Muestra la paga segun el dia de la semana, usando dos listas

import os; os.system("cls")

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
paga = [100, 200, 300, 400, 500, 600, 700]

#n = 3
#print(dias[n], paga[n])

dia = ""
while True:
    dia = input("Dia ? ")
    if dia in dias:
        break

print("Dia        : ", dia)
pos = dias.index(dia)
print("La paga    : ", paga[pos])