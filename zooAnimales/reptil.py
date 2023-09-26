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

    @staticmethod
    def cantidadReptiles(cls):
        return len(Reptil._listado)

    def movimiento(self):
        return

    @classmethod
    def crearIguana(cls, nombre=str, edad=int, genero=str):
        Reptil.iguanas += 1
        iguana = cls(nombre, edad, "humedal", genero, "verde", 3)
        return iguana

    @classmethod
    def crearSerpiente(cls, nombre=str, edad=int, genero=str):
        Reptil.serpiente += 1
        serpiente = cls(nombre, edad, "jungla", genero, "blanco", 1)
        return serpiente
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, _colorEscamas):
        self._colorEscamas = _colorEscamas

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, _largoCola):
        self._largoCola = _largoCola

    
