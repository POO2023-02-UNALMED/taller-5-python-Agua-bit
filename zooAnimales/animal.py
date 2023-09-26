

class Animal:

    def __init__(self, totalAnimales = int, nombre = str, edad = int, habitat = str, genero = str, zona = list):
        self.totalAnimales = totalAnimales
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona

    def movimiento(self):
        return
    
    def totalPorTipo():
        print("Mamiferos: #")
        print("Aves: #")
        print("Reptiles: #")
        print("Peces: #")
        print("Anfibios: #")
    
    def toString():
        print("Mi nombre es #nombre, tengo una edad de #edad, habito en #habitat y mi genero es #genero, la zona en la que me ubico es #zona, en el #zoo")
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, _nombre):
        self._nombre = _nombre