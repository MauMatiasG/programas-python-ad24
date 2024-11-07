# Tercer Examen Parcial

class Jugador:
    def __init__(self, nombre, anonac, sexo, becado):
        self.nombre=nombre
        self.anonac=anonac
        self.sexo=sexo
        self.becado=becado
        self.total=1
        self.conH=0
    def __str__(self):
        return f"Nombre: {self.nombre:<20} AñoNac: {self.anonac:>4}    Sexo: {self.sexo:>6}    Becado: {self.becado:>5}"
    
class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre=nombre
        self.rango=rango
        self.costo=costo
        self.jugadores=list()
    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)
    def totalJugador(self):
        total = 0
        for jugador in self.jugadores:
            total += jugador.total
        return total
    def contar_por_genero(self):
        hombres = sum(1 for jugador in self.jugadores if jugador.sexo == "Hombre")
        mujeres = sum(1 for jugador in self.jugadores if jugador.sexo == "Mujer")
        return hombres, mujeres
    def subtotal_categoria(self):
        subtotal = sum(self.costo for jugador in self.jugadores if jugador.becado.lower() != "becado")
        return subtotal
    def __str__(self):
        return f"{self.nombre} - {self.rango} - ({self.totalJugador()})"
    
class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre=nombre
        self.propietario=propietario
        self.domicilio=domicilio
        self.categorias=list()
    def agregarCategoria(self, categoria):
        self.categorias.append(categoria)
    def contar_total_por_genero(self):
        total_hombres = 0
        total_mujeres = 0
        for categoria in self.categorias:
            hombres, mujeres = categoria.contar_por_genero()
            total_hombres += hombres
            total_mujeres += mujeres
        return total_hombres, total_mujeres
    def total_academia(self):
        total = sum(categoria.subtotal_categoria() for categoria in self.categorias)
        return total

    def __str__(self):
        return f"\nNombre: {self.nombre} \nPropietario: {self.propietario} \nDomicilio: {self.domicilio} "
        

def main():
    import os; os.system("cls")

    #Crear la Academia, con 3 categorias iniciales y sus jugadores
    miacademia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")
    miacademia.agregarCategoria(Categoria("Junior A", "2006/2007/2008",1250))
    miacademia.categorias[0].agregarJugador(Jugador("Alexander Lopez", 2006, "Hombre", "Sin Beca"))
    miacademia.categorias[0].agregarJugador(Jugador("Uriel Puga", 2007, "Hombre", "Becado"))
    miacademia.categorias[0].agregarJugador(Jugador("Alejandra Escalona", 2008, "Mujer", "Sin Beca"))

    miacademia.agregarCategoria(Categoria("Junior B", "2009/2010/2011",850))
    miacademia.categorias[1].agregarJugador(Jugador("Armando Santana", 2009, "Hombre", "Sin Beca"))
    miacademia.categorias[1].agregarJugador(Jugador("Daniel Mijares", 2010, "Hombre", "Sin Beca"))
    miacademia.categorias[1].agregarJugador(Jugador("Antonio Hernandez", 2011, "Mujer", "Becado"))

    miacademia.agregarCategoria(Categoria("Pony A", "2012/2013/2014",700))
    miacademia.categorias[2].agregarJugador(Jugador("Andrea Solis", 2012, "Mujer", "Becado"))
    miacademia.categorias[2].agregarJugador(Jugador("Marissa Hernandez", 2013, "Mujer", "Becado"))
    miacademia.categorias[2].agregarJugador(Jugador("Diana Soto", 2014, "Mujer", "Sin Beca"))
    
    total_hombres, total_mujeres = miacademia.contar_total_por_genero()
 

    # Se imprime un reporte con el total de categorias y sus jugadores
    print("REPORTE DEL CLUB DEPORTIVO\n", miacademia)
    print()
    print("Datos generales de las Categorías")
    print()
    print("Nombre: Junior A      Rango: 2006/2007/2008      Costo: $1,250.00")
    print("Nombre: Junior B      Rango: 2009/2010/2011      Costo: $850.00")
    print("Nombre: Pony A        Rango: 2012/2013/2014      Costo: $700.00")

    print("\nTotal de Categorias  :", len(miacademia.categorias))
    print("Total de Hombres     :", total_hombres)
    print("Total de Mujeres     :", total_mujeres)
    
    print("\nJugadores por Categoria:")
    print()
    for categoria in miacademia.categorias:
        print(categoria)
        for jugador in categoria.jugadores:
            print(jugador)
        print()
        print(f"Subtotal: ${categoria.subtotal_categoria():,.2f}")
        print()

    print(f"\nTotal: ${miacademia.total_academia():,.2f}")

if __name__ == "__main__":
    main()