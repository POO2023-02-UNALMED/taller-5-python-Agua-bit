from zooAnimales.animal import Animal

class Pez(Animal):

    _listado = [] 
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre=str, edad=int,habitat=str, genero=str, colorEscamas=str, cantidadAletas=int):
        Pez._listado.append(self)
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    @staticmethod
    def cantidadPeces():
        return len(Pez._listado)
    
    def movimiento():
        return
    
    @classmethod
    def crearSalmon(cls, nombre=str, edad=int, genero=str):
        Pez.salmones += 1
        salmon = cls(nombre, edad, "oceano", genero, "rojo", 6)
        return salmon
    
    @classmethod
    def crearBacalao(cls, nombre=str, edad=int, genero=str):
        Pez.bacalaos += 1
        bacalao = cls(nombre, edad, "oceano", genero, "gris", 6)
        return bacalao

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, _colorEscamas):
        self._colorEscamas = _colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, _cantidadAletas):
        self._cantidadAletas = _cantidadAletas