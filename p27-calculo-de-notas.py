# Se desea calcular el promedio de 5 calificaciones introducidas por el usuario, 
# luego evaluar el resultado e imprimir un mensaje de acuerdo al promedio obtenido:
# •  >0 y < 6 Quedas reprobado
# • >6 a <7 Pasas de panzazo
# • >7 y <8 Muy bien, pues mejorar
# • >8 y < 9 Excelente sigue así
# • >9 y <=10 Perfecto tu esfuerzo valió la pena

import os; os.system("cls")

print("Calcula el promedio de 5 calificaciones e imprime recultado")

print("Introduce las cinco calificaciones, separadas por un enter")
n1,n2,n3,n4,n5 = float(input()), float(input()), float(input()), float(input()), float(input())

p = (n1 + n2 + n3 + n4 + n5) / 5

if p >= 0 and p < 6:
    print(f"El promedio es {p}, Quedas reprodado")
if p >= 6 and p < 7:
    print(f"El promedio es {p}, Pasas de panzazo")
if p >= 7 and p < 8:
    print(f"El promedio es {p}, Muy bien pues mejorar")
if p >= 8 and p < 9:
    print(f"El promedio es {p}, Excelente sigue asi")
if p >= 9 and p <= 10:
    print(f"El promedio es {p}, Perfecto tu esfuerzo valio la pena")

print("\nProceso terminado ... ")