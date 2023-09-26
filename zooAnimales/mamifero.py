from zooAnimales.animal import Animal

class Mamifero(Animal):

    _listado =[]
    caballos = 0
    leones = 0
    def __init__(self, nombre=str, edad=int,habitat=str, genero=str, pelaje=bool, patas=int):
        Mamifero._listado.append(self)
        super().__init__(nombre, edad,habitat, genero)
        self.pelaje = pelaje
        self.patas = patas

    def cantidadMamiferos():
        return len(Mamifero._listado)
    
    def crearCaballo():
        return
    
    def crearLeon():
        return