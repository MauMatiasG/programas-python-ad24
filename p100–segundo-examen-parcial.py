# Segundo examen parcial

import os; os.system("cls")

print("Mubleria Muebles Dico")
print("Sistema de Procesamiento de Empleados")
print()
print("Captura de datos de los empleados * para terminar:")

empleados = []

while True:
    nm = input("Nombre: ")
    if nm == "*": break
    edad = int(input("Edad: "))
    sex = input("Sexo (h/m): ").lower()
    sueldo = float(input("Sueldo: "))
    pasat = input("Pasatiempos separados por coma y espacio: ").lower().split(", ")
  
    empleado = {
        "Nombre": nm,
        "Edad": edad,
        "Sexo": sex,
        "Sueldo": sueldo,
        "Pasatiempos": pasat
    }
    empleados.append(empleado)


print()
print("Tabla de datos:")

for k in empleados[0].keys():
    print(f"{k:<13}", end="")
print()

for cl in empleados:
    nm = cl['Nombre']
    edad = cl['Edad']
    sex = cl['Sexo']
    sueldo = cl['Sueldo']
    pasat = ', '.join(cl['Pasatiempos'])
    print(f"{nm:<13} {edad:<13} {sex:<10} {sueldo:<12,.3f} {pasat}")
print()

numm = sum(1 for e in empleados if e['Sexo'] == 'm')
numh = sum(1 for e in empleados if e['Sexo'] == 'h')

pasatc = {}
for empleado in empleados:
    for pasatiempo in empleado['Pasatiempos']:
        pasatc[pasatiempo] = pasatc.get(pasatiempo, 0) + 1

Sedades = sum(e['Edad'] for e in empleados)
promedio_edades = Sedades / len(empleados) if len(empleados) > 0 else 0
Ssueldos = sum(e['Sueldo'] for e in empleados)
promedio_sueldos = Ssueldos / len(empleados) if len(empleados) > 0 else 0

maxedad = empleados[0]
minedad = empleados[0]
for empleado in empleados:
    if empleado['Edad'] > maxedad['Edad']:
        maxedad = empleado
    if empleado['Edad'] < minedad['Edad']:
        minedad = empleado


print("Resumen:")
print("Empleados :", len(empleados))
print("Mujeres   :", numm)
print("Hombres   :", numh)
print("Pasatiempos:", ', '.join(f"{k}/{v}" for k, v in pasatc.items()))
print(f"Edad -> suma: {Sedades}, Promedio: {promedio_edades:.1f}")
print(f"Sueldo -> suma: {Ssueldos:,.2f}, promedio: {promedio_sueldos:,.2f}")
print(f"{maxedad['Nombre']} de {maxedad['Edad']} es el mayor, {minedad['Nombre']} de {minedad['Edad']} es el menor.")



