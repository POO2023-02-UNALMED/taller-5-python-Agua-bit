from zooAnimales.animal import Animal

class Mamifero(Animal):

    _listado =[]
    caballos = 0
    leones = 0

    def __init__(self, nombre=str, edad=int,habitat=str, genero=str, pelaje=bool, patas=int):
        self._nombre = nombre
        self._edad = edad
        self._habitat =habitat
        self._genero = genero
        self.pelaje = pelaje
        self.patas = patas

    def cantidadMamiferos():
        return
    
    def crearCaballo():
        return
    
    def crearLeon():
        return