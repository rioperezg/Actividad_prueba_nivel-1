from Coche import Coche
class Formula1(Coche):
    def __init__(self, nbast, color, ruedas, velocidad, cilindrada, Equipo):
        super().__init__(nbast, color, ruedas, velocidad, cilindrada)
        self.Equipo = Equipo
    def __str__(self):
        return "El formula1 pertenece a {}".format(self.Equipo)
    