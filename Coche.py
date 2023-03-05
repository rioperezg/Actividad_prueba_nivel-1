from Database import Vehiculo
class Coche(Vehiculo):
    def __init__(self, nbast, color, ruedas, velocidad, cilindrada):
        super().__init__(nbast, color, ruedas, velocidad, cilindrada)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        print("El coche tiene una velocidad de {} km/h y una cilindrada de {} cc".format(self.velocidad, self.cilindrada))
