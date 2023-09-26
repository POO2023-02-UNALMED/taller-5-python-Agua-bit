

class Zoologico():
    
    _zonas= []
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

    def agregarZonas(self, zona):
        self._zonas.append(zona)


    def cantidadTotalAnimales(self):
        return