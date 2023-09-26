from zooAnimales.animal import Animal


class Reptil(Animal):
    
    _listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre=str, edad=int,habitat=str, genero=str, colorEscamas=str, largoCola=int):
        super().__init__(nombre, edad,habitat, genero)
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
