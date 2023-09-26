import zooAnimales

class Animal:

    _totalAnimales = 0
    _zona= ""
    def __init__(self,  nombre = str, edad = int, habitat = str, genero = str):
        Animal._totalAnimales += 1 
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero

    def movimiento(self):
        return
    
    @staticmethod
    def totalPorTipo():
        return "Mamiferos: " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos) + "\n" "Aves : " + str(zooAnimales.ave.Ave.cantidadAves) + "\n" "Reptiles: " + str(zooAnimales.reptil.Reptiles.cantidadReptiles) + "\n" "Peces: " + str(zooAnimales.pez.Pez.cantidadPeces) + "\n" "Anfibios: " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios)
    
        print("Anfibios: #")
    
    def toString():
        print("Mi nombre es #nombre, tengo una edad de #edad, habito en #habitat y mi genero es #genero, la zona en la que me ubico es #zona, en el #zoo")
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, _nombre):
        self._nombre = _nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, _edad):
        self._edad = _edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, _habitat):
        self._habitat = _habitat

    def getGenero(self):
        return self._genero
    
    def setGenero(self, _genero):
        self._genero = _genero

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    @classmethod
    def setTotalAnimales(cls, _totalAnimales):
        cls._totalAnimales = _totalAnimales

    
