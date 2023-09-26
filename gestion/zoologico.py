

class Zoologico():
    
    _zonas= []
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        return 
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, _nombre):
        self._nombre = _nombre

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, _ubicacion):
        self._ubicacion = _ubicacion