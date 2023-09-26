class Zona:

    def __init__(self, nombre, zoo = None):
        self._animales = []
        self._nombre = nombre
        self._zoo = zoo
        

    def agregarAnimales(self, animales):
        self._animales.append(animales)

    def cantidadAnimales(self):
        return len(self._animales)
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, _nombre):
        self._nombre = _nombre

    def getZoo(self):
        return self._zoo
    
    def setZoo(self, _zoo):
        self._zoo = _zoo
