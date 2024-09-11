# Computación Aplicada Primer examen parcial

import os

TT = 0

while(True):
    os.system("cls")

    print("Universidad Patito SA de CV")
    print("\nSistema de inscripción Congreso de Sistemas")

    des = 0

    u1 = 100
    u2 = 200
    u3 = 500

    p1 = 600
    p2 = 800 
    p3 = 900

    usuario = int(input("\nTipo de usuario\n[1] Alumno $100\n[2] Trabajador $200\n[3] Docente $500\nSeleccione una opcione: "))
    paquete = int(input("\nTipo de paquete\n[1] Solo conferencias $600\n[2] Con eventos sociales $800\n[3] Con kit de acceso $900\nSeleccione una opcion: "))
    cantidad = int(input("\nCantidad ? "))

    if usuario == 1 and paquete == 1:
        des = 0.20
        sub = (u1 + p1) * cantidad 
        tot = sub - (sub * des)
        print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Alumno, Tipo de paquete: Solo conferencias")
        print(f"Subtotal: {sub} con un descuento de: {(sub * des):.2f} (20.0%) y un total de: {tot}")

    elif usuario == 1 and paquete == 2:
        des = 0.20
        sub = (u1 + p2) * cantidad 
        tot = sub - (sub * des)
        print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Alumno, Tipo de paquete: Con eventos sociales")
        print(f"Subtotal: {sub} con un descuento de: {(sub * des):.2f} (20.0%) y un total de: {tot}")

    elif usuario == 1 and paquete == 3:
        des = 0.20
        sub = (u1 + p3) * cantidad 
        tot = sub - (sub * des)
        print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Alumno, Tipo de paquete: Con kit de acceso")
        print(f"Subtotal: {sub} con un descuento de: {(sub * des):.2f} (20.0%) y un total de: {tot}")

    elif usuario == 2 and paquete == 1:
        des = 0.10
        sub = (u2 + p1) * cantidad 
        tot = sub - (sub * des)
        print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Trabajador, Tipo de paquete: Solo conferencias")
        print(f"Subtotal: {sub} con un descuento de: {(sub * des):.2f} (10.0%) y un total de: {tot}")

    elif usuario == 2 and paquete == 2:
        des = 0.10
        sub = (u2 + p2) * cantidad 
        tot = sub - (sub * des)
        print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Trabajador, Tipo de paquete: Con eventos sociales")
        print(f"Subtotal: {sub} con un descuento de: {(sub * des):.2f} (10.0%) y un total de: {tot}")

    elif usuario == 2 and paquete == 3:
        des = 0.10
        sub = (u2 + p3) * cantidad 
        tot = sub - (sub * des)
        print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Trabajador, Tipo de paquete: Con kit de acceso")
        print(f"Subtotal: {sub} con un descuento de: {(sub * des):.2f} (10.0%) y un total de: {tot}")

    elif usuario == 3 and paquete == 1:
        des = 0.05
        sub = (u3 + p1) * cantidad 
        tot = sub - (sub * des)
        print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Docente, Tipo de paquete: Solo conferencias")
        print(f"Subtotal: {sub} con un descuento de: {(sub * des):.2f} (5.0%) y un total de: {tot}")

    elif usuario == 3 and paquete == 2:
        des = 0.05
        sub = (u3 + p2) * cantidad 
        tot = sub - (sub * des)
        print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Docente, Tipo de paquete: Con eventos sociales")
        print(f"Subtotal: {sub} con un descuento de: {(sub * des):.2f} (5.0%) y un total de: {tot}")

    elif usuario == 3 and paquete == 3:
        des = 0.05
        sub = (u3 + p3) * cantidad 
        tot = sub - (sub * des)
        print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Docente, Tipo de paquete: Con kit de acceso")
        print(f"Subtotal: {sub} con un descuento de: {(sub * des):.2f} (5.0%) y un total de: {tot}")
    else: 
        print("\nIntroduce una opcion valida")  

    TT = TT + tot

    if input("\nDeseas continuar (S/N) ").upper().startswith("N"): break

print(f"\nImporte Total de la venta: {TT:.2f}")

print("\nProceso terminado ...")