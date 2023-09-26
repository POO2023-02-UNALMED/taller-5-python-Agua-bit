

class Zoologico():
    
    _zonas= []
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def agregarZonas(self, zona):
        self._zonas.append(zona)
    
    @classmethod
    def getZona(cls):
        return cls._zonas
    
    @classmethod
    def setZona(cls, zona):
        cls._zonas = zona

    def cantidadTotalAnimales(self):
        i = 0
        for e in self._zonas:
            i += e.cantidadAnimales()
        return i
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, _nombre):
        self._nombre = _nombre

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, _ubicacion):
        self._ubicacion = _ubicacion