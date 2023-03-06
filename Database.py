import csv
import config
from Coche import Coche
from Camioneta import Camioneta
from Bicicleta import Bicicleta
from Motocicleta import Motocicleta
from Quad import Quad
from Formula1 import Formula1
from vehiculo import Vehiculo

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
    def crear(nbast, color, ruedas, velocidad, Cilindrada, Carga, Tipo, speed, cilindrada, carga):
        vehiculo = Vehiculo(nbast, color, ruedas, velocidad, Cilindrada, Carga, Tipo, speed, cilindrada, carga)
        Vehiculos.Vehiculos.append(vehiculo)
        Vehiculos.guardar()
        return vehiculo
    
    @staticmethod
    def crear_Coche(nbast, color, ruedas, velocidad, Cilindrada):
        car = Coche(nbast, color, ruedas, velocidad, Cilindrada)
        Vehiculos.Vehiculos.append(car)
        Vehiculos.guardar()
        return car

    @staticmethod
    def crear_Cam(nbast, color, ruedas, velocidad, Cilindrada, Carga):
        van = Camioneta(nbast, color, ruedas, velocidad, Cilindrada, Carga)
        Vehiculos.Vehiculos.append(van)
        Vehiculos.guardar()
        return van

    @staticmethod
    def crear_F1(nbast, color, ruedas, velocidad, Cilindrada, Equipo):
        For1 = Formula1(nbast, color, ruedas, velocidad, Cilindrada, Equipo)
        Vehiculos.Vehiculos.append(For1)
        Vehiculos.guardar()
        return For1

    @staticmethod
    def crear_Bici(nbast, color, ruedas, tipo):
        bike = Bicicleta(nbast, color, ruedas, tipo)
        Vehiculos.Vehiculos.append(bike)
        Vehiculos.guardar()
        return bike

    @staticmethod
    def crear_Moto(nbast, color, ruedas, tipo, velocidad, cilindrada):
        Motbike = Motocicleta(nbast, color, ruedas, tipo, velocidad, cilindrada)
        Vehiculos.Vehiculos.append(Motbike)
        Vehiculos.guardar()
        return Motbike

    @staticmethod
    def crear_Quad(nbast, color, ruedas, velocidad, Cilindrada, tipo, carga):
        quad = Quad(nbast, color, ruedas, velocidad, Cilindrada, tipo, carga)
        Vehiculos.Vehiculos.append(quad)
        Vehiculos.guardar()
        return quad

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

