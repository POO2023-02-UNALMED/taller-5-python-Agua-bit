from zooAnimales.animal import Animal


class Reptil(Animal):
    
    _listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre=str, edad=int,habitat=str, genero=str, colorEscamas=str, largoCola=int):
        Reptil._listado.append(self)
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    def cantidadReptiles(self):
        return len(Reptil._listado)

    def movimiento(self):
        return

    def crearIguana(self):
        return

    def crearSerpiente(self):
        return
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, _colorEscamas):
        self._colorEscamas = _colorEscamas

    def getLargoColo(self):
        return self._largoCola
    
    def setLargoCola(self, _largoCola):
        self._largoCola = _largoCola
