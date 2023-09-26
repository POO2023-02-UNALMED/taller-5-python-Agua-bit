from zooAnimales.animal import Animal


class Reptil(Animal):
    
    _listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre=str, edad=int,habitat=str, genero=str, colorEscamas=str, largoCola=int):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola

    def cantidadReptiles(self):
        return

    def movimiento(self):
        return

    def crearIguana(self):
        return

    def crearSerpiente(self):
        return
