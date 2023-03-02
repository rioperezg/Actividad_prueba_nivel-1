from Vehiculo import Vehiculo
from Coche import Coche
from Camioneta import Camioneta
from Bicicleta import Bicicleta
from Motocicleta import Motocicleta
class Vehiculos:
    Vehiculos = []
    def lista_de_Vehiculos():
        Porsche = Coche.__init__("Amarillo", 4, 200, 800)
        Vehiculos.append(Porsche)
        Renault = Camioneta.__init__("Blanco", 6, 150, 800, 1000)
        Vehiculos.append(Renault)
        Bici = Bicicleta.__init__("Rojo", 2, "Deportiva")
        Vehiculos.append(Bici)
        Yamaha = Motocicleta.__init__("Amarillo", 2, 200, 750)
        Vehiculos.append(Yamaha)
    def Catalogar(Lista = Vehiculos):
        for Lista in Lista:
            print(Lista)

