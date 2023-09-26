from zooAnimales.animal import Animal

class Pez(Animal):

    _listado = [] 
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre=str, edad=int,habitat=str, genero=str, colorEscamas=str, cantidadAletas=int):
        Pez._listado.append(self)
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas

    def cantidadPeces():
        return len(Pez._listado)
    
    def movimiento():
        return
    
    def crearIguana():
        return
    
    def crearSerpiente():
        return