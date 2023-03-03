from Coche import Coche
class Formula(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, Equipo):
        super().__init__(color, ruedas, velocidad, cilindrada, Equipo)
        self.Equipo = Equipo
    def __str__(self):
        return "El formula1 pertenece a {}".format(self.Equipo)
    