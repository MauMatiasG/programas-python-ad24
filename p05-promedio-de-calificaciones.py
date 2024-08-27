# Calcula el promedio de 3 calificaciones 

print("Calculando el promedio de 3 calificaciones \n")

print("Introduce 3 calificaciones enteras, separadas por un espacio")
c1,c2,c3 = input().split()
c1,c2,c3 = [int(c1),int(c2),int(c3)]

suma = ( c1 + c2 + c3 )
prom = (c1+c2+c3)/3

print(f"Las calificaciones fueron {c1}, {c2}, {c3}")
print(f"La suma es {suma}")
print(f"El promedio es {prom}")