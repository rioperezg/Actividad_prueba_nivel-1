from Coche import Coche
class Camioneta(Coche):
    def __init__(self, nbast, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(nbast, color, ruedas, velocidad, cilindrada, carga)
        self.carga = carga
    def __str__(self):
        return "La camioneta tiene un carga de {}".format(self.carga)