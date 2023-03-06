from Database import Vehiculos
from Database import Vehiculo
import Coche
import Camioneta    
import Formula1
import Bicicleta
import Motocicleta
import Quad
def iniciar():
    while True:

        print("=========================")
        print("  Bienvenido  al Gestor  ")
        print("=========================")
        print("[1] Listar los vehiculos ")
        print("[2] Buscar un vehiculo   ")
        print("[3] Añadir un vehiculo   ")
        print("[4] Modificar un vehiculo")
        print("[5] Borrar un vehiculo   ")
        print("[6] Catalogar un vehiculo")
        print("[7] Cerrar el Gestor     ")
        print("=========================")

        opcion = input("> ")

        if opcion == "1":
            print("Listando los vehiculos...\n")
            for vehiculo in Vehiculos.Vehiculos:
                print(vehiculo)

        if opcion == "2":
            print("Buscando los vehiculos...\n")
            nbast = input("Numero de bastidor(2 int y 1 chr) > ")
            vehiculo = Vehiculos.buscar(nbast=nbast)
            print(vehiculo) if vehiculo else print("Vehiculo no encontrado.")

        if opcion == "3":
            print("Añadiendo un vehiculo...\n")
            print("Tipo de vehiculo?:\n(Coche, Camioneta, Formula1, Bicicleta, Motocicleta, Quad)")
            Type = input(" > ")
            if Type == "Coche":
                nbast = input("Numero de bastidor(2 int y 1 chr) > ")
                color = input("Color > ")
                ruedas = input("Numero de ruedas > ")
                velocidad = input("Velocidad del coche(km/h) > ")
                Cilindrada = input("Cilindrada del coche(cc) > ")
                vehiculo = Vehiculos.crear_Coche(nbast,color,ruedas,velocidad,Cilindrada)
                print("Vehiculo añadido")
            elif Type == "Camioneta":
                nbast = input("Numero de bastidor(2 int y 1 chr) > ")
                color = input("Color > ")
                ruedas = input("Numero de ruedas > ")
                velocidad = input("Velocidad del coche(km/h) > ")
                Cilindrada = input("Cilindrada del coche(cc) > ")
                Carga = input("Carga de la camioneta(kg) > ")
                vehiculo = Vehiculos.crear_Cam(nbast,color,ruedas,velocidad,Cilindrada,Carga)
                print("Vehiculo añadido")
            elif Type == "Formula1":
                nbast = input("Numero de bastidor(2 int y 1 chr) > ")
                color = input("Color > ")
                ruedas = input("Numero de ruedas > ")
                velocidad = input("Velocidad del coche(km/h) > ")
                Cilindrada = input("Cilindrada del coche(cc) > ")
                Equipo = input("Equipo del Formula1 > ")
                vehiculo = Vehiculos.crear_F1(nbast,color,ruedas,velocidad,Cilindrada,Equipo)
                print("Vehiculo añadido")
            elif Type == "Bicicleta":
                nbast = input("Numero de bastidor(2 int y 1 chr) > ")
                color = input("Color > ")
                ruedas = input("Numero de ruedas > ")
                tipo = input("Tipo de Bicicleta > ")
                vehiculo = Vehiculos.crear_Bici(nbast,color,ruedas,tipo)
                print("Vehiculo añadido") 
            elif Type == "Motocicleta":
                nbast = input("Numero de bastidor(2 int y 1 chr) > ")
                color = input("Color > ")
                ruedas = input("Numero de ruedas > ")
                tipo = input("Tipo de Bicicleta > ")
                speed = input("Velocidad de la motocicleta(km/h) > ")
                cilindrada = input("Cilindrada de la motocicleta(cc) > ")
                vehiculo = Vehiculos.crear_Moto(nbast,color,ruedas,tipo,speed,cilindrada)
                print("Vehiculo añadido") 
            elif Type == "Quad":
                nbast = input("Numero de bastidor(2 int y 1 chr) > ")
                color = input("Color > ")
                ruedas = input("Numero de ruedas > ")
                velocidad = input("Velocidad del coche(km/h) > ")
                Cilindrada = input("Cilindrada del coche(cc) > ")
                tipo = input("Tipo de Bicicleta > ")
                carga = input("Carga del quad(kg) > ")
                vehiculo = Vehiculos.crear_Quad(nbast,color,ruedas,velocidad,Cilindrada,tipo,carga)
                print("Vehiculo añadido")
            
        if opcion == 4:
            print("Modificando un vehiculo...\n")
            nbast = input("Introduzca el numero de bastidor para encontrar el vehiculo(2 int y 1 chr) > ")
            vehiculo = Vehiculos.buscar(nbast)
            if vehiculo:
                Vehiculos.modificar(nbast)
            else:
                print("Vehiculo no encontrado")

        if opcion == 5:
            print("Borrando un Vehiculo...\n")
            nbast = input("introduzca el numero de bastidor para boorar el vehiculo(2 int y 1 chr) > ")
            if vehiculo:
                Vehiculos.borrar(nbast)
            else:
                print("Vehiculo no encontrado")

        if opcion == 6:
            print("Catalogando un vehiculo...\n")
            ruedas = input("Numero de ruedas > ")
            Vehiculos.catalogar(ruedas)

        if opcion == 7:
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...") 

print(iniciar())                    