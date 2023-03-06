from vehiculo import Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, nbast, color, ruedas, tipo):
        super().__init__(nbast, color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return "La bicicleta es de tipo {}".format(self.tipo)