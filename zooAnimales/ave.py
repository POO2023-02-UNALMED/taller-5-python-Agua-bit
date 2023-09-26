from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre=str, edad=int,habitat=str, genero=str, colorPlumas=str):
        super().__init__(nombre, edad,habitat, genero)
        self._genero = genero
        self.colorPlumas = colorPlumas

    def cantidadAveso():
        return
    
    def movimiento():
        return
    
    def crearHalcon():
        return 
    
    def crearAguila():
        return