from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre=str, edad=int,habitat=str, genero=str, colorPlumas=str):
        Ave._listado.append(self)
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas

    @staticmethod
    def cantidadAves(cls):
        return len(Ave._listado)
    
    def movimiento():
        return
    
    @classmethod
    def crearHalcon(cls, nombre=str, edad=int, genero=str):
        Ave.halcones += 1
        halc = cls(nombre, edad, "montanas", genero, "cafe glorioso")
        return halc
    
    @classmethod
    def crearAguila(cls, nombre=str, edad=int, genero=str):
        Ave.aguilas += 1
        agui = cls(nombre, edad, "montanas", genero, "blanco y amarillo")
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, _colorPlumas):
        self._colorPlumas = _colorPlumas