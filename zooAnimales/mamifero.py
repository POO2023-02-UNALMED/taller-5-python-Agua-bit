from zooAnimales.animal import Animal

class Mamifero(Animal):

    _listado =[]
    caballos = 0
    leones = 0
    def __init__(self, nombre=str, edad=int,habitat=str, genero=str, pelaje=bool, patas=int):
        Mamifero._listado.append(self)
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas

    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero._listado)
    
    @classmethod
    def crearCaballo(cls, nombre=str, edad=int, genero=str):
        cab = cls(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1
        return cab

    @classmethod
    def crearLeon(cls, nombre=str, edad=int, genero=str):
        Mamifero.leones += 1
        le = cls(nombre, edad, "selva", genero, True, 4)
        return le
    
    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, _pelaje):
        self._pelaje = _pelaje

    def getPatas(self):
        return self._patas
    
    def setPatas(self, _patas):
        self._patas = _patas