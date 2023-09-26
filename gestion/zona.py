class Zona:

    def __init__(self, nombre, zoo):
        self._animales = []
        self.nombre = nombre
        self.zoo = zoo
        

    def agregarAnimales(self, animales):
        self._animales.append(animales)

    def cantidadAnimales(self):
        return len(self._animales)