# Creamos una clase Empleado con atributos y metodos
# Ampliamos la clase

# Codigo de clase
class Empleado: 
    def __init__(self, nombre, edad, sexo, casado):
        self.nombre = nombre
        self.edad= edad
        self.sexo= sexo
        self.casado= casado
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {"Mujer" if self.sexo=="M" else "Hombre"}, Casado: {"Casad@" if self.casado else "Solter@"}"
    
# Programa Principal
import os; os.system("cls")

emp01 = Empleado("Carlos Castaneda", 35, "H", True)
print(f"Nombre      : {emp01.nombre}")
print(f"Edad        : {emp01.edad}")
print(f"Sexo        : {emp01.sexo}")
print(f"Casado      : {emp01.casado}")
print(f"Empleado    : {emp01}")
print()
emp02 = Empleado("Rocio Soto", 32, "M", True)
print(f"Nombre      : {emp02.nombre}")
print(f"Edad        : {emp02.edad}")
print(f"Sexo        : {emp02.sexo}")
print(f"Casado      : {emp02.casado}")
print(f"Empleado    : {emp02}")
print()
emp03 = Empleado("Rebeca Soto", 22, "M", True)
print(f"Empleado    : {emp03}")

pedad = (emp01.edad + emp02.edad + emp03.edad) / 3
print(f"Promedio de edad de los empleados {pedad:.2f}")