class Zona:

    def __init__(self, nombre, zoo):
        self._animales = []
        self.nombre = nombre
        self.zoo = zoo
        

    def agregarAnimales(self, animales):
        self._animales.append(animales)

    def cantidadAnimales(self):
        return len(self._animales)
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, _nombre):
        self._nombre = _nombre
