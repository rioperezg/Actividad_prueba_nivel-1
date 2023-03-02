from Vehiculo import Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas, tipo)
        self.tipo = tipo
    def __str__(self):
        return "La bicicleta es de tipo {}".format(self.tipo)