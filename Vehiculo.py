class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "El vehiculo es de color {}, y tiene {} ruedas".format(self.color, self.ruedas)


    