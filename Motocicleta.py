from Bicicleta import Bicicleta
class Motocicleta(Bicicleta):
    def __init__(self, nbast, color, ruedas, tipo, speed, cilindrada):
        super().__init__(nbast, color, ruedas, tipo, speed, cilindrada)
        self.speed = speed
        self.cilindrada = cilindrada
    def __str__(self):
        return "La motocicleta tiene una velocidad de {} y una cilindrada de {}".format(self.speed, self.cilindrada)