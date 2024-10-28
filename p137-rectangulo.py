# Modelamos un rectangulo con atributos: largo, ancho y metodos: Area, Perimetro

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def obtenerArea(self):
        return self.largo * self.ancho
    def obtenerPerimetro(self):
        return 2 * (self.largo + self.ancho)
    def __str__(self):
        return f"Rectangulo [ Largo = {self.largo}, Ancho = {self.ancho}, Area = {self.obtenerArea():.2f}, Perimetro = {self.obtenerPerimetro():.2f}]"
    
import os; os.system("cls")

r1 = Rectangulo(12,3.4)
print("\nRectangulo 1")
print(f"Largo      : {r1.largo}")
print(f"Ancho      : {r1.ancho}")
print(f"Area       : {r1.obtenerArea():.2f}")
print(f"Perimetro  : {r1.obtenerPerimetro():.2f}")


r2 = Rectangulo(5.6, 7.8)
print("\nRectangulo 1")
print(r2)


