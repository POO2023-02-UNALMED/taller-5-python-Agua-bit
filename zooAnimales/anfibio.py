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
        
    def cantidadAnfibios():
        return len(Anfibio._listado)
    
    def movimiento():
        return
    
    def crearRana():
        return
    
    def crearSalamandra():
        return
    
    
    