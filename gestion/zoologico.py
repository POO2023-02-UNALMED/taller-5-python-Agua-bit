

class Zoologico():
    
    _zonas= []
    def __init__(self, nombre, ubicacion, zonas):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = zonas

    def agregarZonas(self, zona):
        self._zonas.append(zona)


    def cantidadTotalAnimales(self):
        return