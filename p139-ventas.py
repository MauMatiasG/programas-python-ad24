# Aplicacion orientado a objetos que simula las ventas de una tienda

class Venta:
    def __init__(self, articulo, cantidad, precio):
        self.articulo=articulo
        self.cantidad=cantidad
        self.precio=precio
        self.total=cantidad * precio
    def __str__(self):
        return f"Articulo: {self.articulo:<15} Cantidad: {self.cantidad:>10,.2f} Total: {self.total:>10,.2f}"
    
class Cliente:
    def __init__(self, rfc, nombre, domicilio, correo):
        self.rfc=rfc
        self.nombre=nombre
        self.domicilio=domicilio
        self.correo=correo
        self.ventas=list()
    def agregarVenta(self, venta):
        self.ventas.append(venta)
    def totalVentas(self):
        total=0
        for venta in self.ventas:
            total += venta.total
        return total

    def __str__(self):
        return f"Cliente [Nombre = {self.nombre:<20} RFC: {self.rfc:<12} Domicilio: {self.domicilio:<20} Correo: {self.correo:<20}] - Total Ventas: {self.totalVentas():,.2f}"
    
class Tienda:
    def __init__(self, nombre, domicilio, propiedad):
        self.nombre=nombre
        self.domicilio=domicilio
        self.propiedad=propiedad
        self.clientes=list()
    def agregarCliente(self, cliente):
        self.clientes.append(cliente)
    def totalVentas(self):
        total = 0
        for cliente in self.clientes:
            total += len(cliente.ventas)
        return total
    def totalImporteVentas(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.totalVentas()
        return total
    def __str__(self):
        return f"Tienda [Nombre: {self.nombre} Domicilio: {self.domicilio} Propietario: {self.propiedad}] - Total Ventas: {self.totalImporteVentas():,.2f}"
        
def capturaCliente():
    print("Dame los datos del cliente")
    rfc = input("RFC: ")
    nombre = input("Nombre: ")
    domicilio= input("Domicilio: ")
    correo= input("Correo:  ")
    cliente = Cliente(rfc, nombre, domicilio, correo)
    return cliente

def agregarVentas(cliente):
    print("Captura de ventas ", cliente.nombre)
    while True:
        articulo = input("Articulo: ")
        if articulo == "": break
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        cliente.agregarVenta(Venta(articulo, cantidad, precio))

def main():
    import os; os.system("cls")
    #Crear la tienda, con 3 clientes iniciales y sus ventas
    mitienda = Tienda("Ferreteria las lomas", "Av Luis Moya 345", "Carlos Castaneda")
    mitienda.agregarCliente(Cliente("CARC711202", "Carlos Casatenda","Av Mexico 115", "Castr@uaz.edu.mx"))
    mitienda.clientes[0].agregarVenta(Venta("Martillo", 10, 200))
    mitienda.clientes[0].agregarVenta(Venta("Pala", 5, 450))
    mitienda.clientes[0].agregarVenta(Venta("Cinta Aislar", 15, 35))
    mitienda.agregarCliente(Cliente("JOSE850324", "Jose Perez", "Sierra Nevada 345", "jose@gmail.com"))
    mitienda.clientes[1].agregarVenta(Venta("Pinzas", 10, 650.33))
    mitienda.clientes[1].agregarVenta(Venta("Thiner", 50, 65))
    mitienda.agregarCliente(Cliente("SOBR731223", "Rocio Soto", "Sierra Tecuan 345", "rocio@gmail.com"))
    mitienda.clientes[2].agregarVenta(Venta("Talache", 2, 1650.33))
    #Permite al usuario capturar un cliente y sus ventas
    cliente = capturaCliente()
    agregarVentas(cliente)
    mitienda.agregarCliente(cliente)
    # Se imprime un reporte con el total de clientes y sus ventas
    print("\nReporte de Ventas : ", mitienda)
    print("Clientes          :", len(mitienda.clientes))
    print("Ventas            :", mitienda.totalVentas())
    print("\nClientes:")
    for cliente in mitienda.clientes:
        print(cliente)
        for venta in cliente.ventas:
            print(venta)
        print()

if __name__ == "__main__":
    main()