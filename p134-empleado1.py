# Creamos una clase Empleado con atributos y metodos

# Codigo de clase
class Empleado: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad= edad
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
# Programa Principal
import os; os.system("cls")
emp01 = Empleado("Carlos Castaneda", 35) # Creamos una instancia
emp02 = Empleado("Juan Perez", 66) # Creamos una instancia

print("\nDatos del Empleado 1")
print(f"Nombre   : {emp01.nombre}")
print(f"Edad     : {emp01.edad}")
print(f"Empleado : {emp01}")
emp01.edad=40
print(f"Empleado : {emp01}")

print("\nDatos del Empleado 2")
print(f"Nombre   : {emp02.nombre}")
print(f"Edad     : {emp02.edad}")
print(f"Empleado : {emp02}")

