from Coche import Coche
from Bicicleta import Bicicleta
class Quad(Coche, Bicicleta):
    def __init__(self, color, ruedas, velocidad, cilindrada, tipo, carga):
        super().__init__(color, ruedas, velocidad, cilindrada, tipo, carga)
        self.carga = carga
    def __str__(self):
        return "El Quad tiene una carga de {}".format(self.carga)