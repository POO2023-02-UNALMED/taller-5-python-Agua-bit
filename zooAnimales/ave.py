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
    def cantidadAves():
        return len(Ave._listado)
    
    def movimiento():
        return
    
    def crearHalcon():
        return 
    
    def crearAguila():
        return
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, _colorPlumas):
        self._colorPlumas = _colorPlumas