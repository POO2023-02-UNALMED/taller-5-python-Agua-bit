from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre=str, edad=int,habitat=str, genero=str, colorPiel=str, venenoso=bool):
        Anfibio._listado.append(self)
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    @staticmethod 
    def cantidadAnfibios():
        return len(Anfibio._listado)
    
    def movimiento():
        return
    
    @classmethod
    def crearRana(cls, nombre=str, edad=int, genero=str):
        Anfibio.ranas += 1
        rana =cls(nombre, edad, "selva", genero, "rojo", True)
        return rana
    
    @classmethod
    def crearSalamandra(cls, nombre=str, edad=int, genero=str):
        Anfibio.salamandras += 1
        sal = cls(nombre, edad, "selva", genero, "negro y amarillo", False)
        return sal
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, _color):
        self._colorPiel = _color

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, _venenoso):
        self._venenoso = _venenoso
    

    
    