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
        return "Mamiferos: " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) + "\nAves : " + str(zooAnimales.ave.Ave.cantidadAves()) + "\nReptiles: " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) + "\nPeces: " + str(zooAnimales.pez.Pez.cantidadPeces()) + "\nAnfibios: " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())
    
    def toString(self):
        if self._zona !="":
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getNombre()}, en el {self._zona.getZoo().getNombre()}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
    
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

    
