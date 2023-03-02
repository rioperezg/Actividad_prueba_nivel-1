from Vehiculo import Vehiculo
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        print("El coche tiene una velocidad de {} km/h y una cilindrada de {} cc".format(self.velocidad, self.cilindrada))
