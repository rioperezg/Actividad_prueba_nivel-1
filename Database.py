from Vehiculo import Vehiculo
from Coche import Coche
from Camioneta import Camioneta
from Bicicleta import Bicicleta
from Motocicleta import Motocicleta
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "El vehiculo es de color {}, y tiene {} ruedas".format(self.color, self.ruedas)
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
    @Catalogar("ruedas")
    def Catalogo(ruedas):


class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"

    def to_dict(self):
        return {'dni': self.dni, 'nombre': self.nombre, 'apellido': self.apellido}


class Clientes:

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar(dni, nombre, apellido):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]

    @staticmethod
    def borrar(dni):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))




