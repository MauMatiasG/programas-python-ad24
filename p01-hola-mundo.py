# p01-hola-mundo - Recibe datos del usuario y los imprime en pantalla

nombre =input("Dame tu nombre ? ")
edad = int( input("Edad ? "))
peso = float( input("Peso ? "))

print(nombre)
print(edad)
print(peso)

print(f"{nombre} bienvenido a Python, tu edad es {edad} tu peso es {peso}")

print(type(nombre))
print(type(edad))
print(type(peso))
