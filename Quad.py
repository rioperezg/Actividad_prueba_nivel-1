from Coche import Coche
from Bicicleta import Bicicleta
class Quad(Coche, Bicicleta):
    def __init__(self, nbast, color, ruedas, velocidad, cilindrada, tipo, carga):
        super(Coche).__init__(nbast, color, ruedas, velocidad, cilindrada)
        super(Bicicleta).__init__(nbast, color, ruedas, tipo)
        self.carga = carga
    def __str__(self):
        return "El Quad tiene una carga de {}".format(self.carga)