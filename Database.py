import csv
import config

class Vehiculo:
    def __init__(self, nbast, color, ruedas):
        self.nbast = nbast
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "El vehiculo es de color {}, y tiene {} ruedas".format(self.color, self.ruedas)
class Vehiculos:
    Vehiculos = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for nbast, color, ruedas in reader:
            vehiculo = Vehiculo(nbast, color, ruedas)
            Vehiculos.append(vehiculo)

    @staticmethod
    def catalogar(ruedas):
        sum = 0
        for vehiculo in Vehiculos.Vehiculos:
            if vehiculo.ruedas == ruedas:
                sum += 1
                print(vehiculo)
        return "se han encontrado {} vehiculos con {} ruedas".format(sum, ruedas)

    @staticmethod
    def buscar(nbast):
        for vehiculo in Vehiculos.Vehiculos:
            if vehiculo.nbast == nbast:
                return vehiculo

    @staticmethod
    def crear(nbast, color, ruedas):
        vehiculo = Vehiculo(nbast, color, ruedas)
        Vehiculos.Vehiculos.append(vehiculo)
        Vehiculos.guardar()
        return vehiculo

    @staticmethod
    def modificar(nbast, color, ruedas):
        for indice, vehiculo in enumerate(Vehiculos.Vehiculos):
            if vehiculo.nbast == nbast:
                Vehiculos.Vehiculos[indice].color = color
                Vehiculos.Vehiculos[indice].ruedas = ruedas
                Vehiculos.guardar()
                return Vehiculos.Vehiculos[indice]

    @staticmethod
    def borrar(nbast):
        for indice, vehiculo in enumerate(Vehiculos.Vehiculos):
            if vehiculo.nbast == nbast:
                vehiculo = Vehiculos.Vehiculos.pop(indice)
                Vehiculos.guardar()
                return vehiculo

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Vehiculos.Vehiculos:
                writer.writerow((vehiculo.nbast, vehiculo.color, vehiculo.ruedas))            

