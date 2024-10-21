# Funcion que dibuja un cuadro de r x c, del caracter deseado
import os

def cuadro(r, c, car):
    for i in range(1, r+1):
        for j in range(1, c+1):
            print(car,end="")
        print()

#Principal
os.system("cls")
#cuadro(5,25,"$")
#cuadro(10,10,"@")
r = int(input("Cuantos renglones ? "))
c = int(input("Cuantas columnas  ? "))
car = input("De que caracter     ? ")
cuadro(r, c, car)