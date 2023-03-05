from Database import Vehiculos
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
            print("Listando los clientes...\n")
            for vehiculo in Vehiculos.Vehiculos:
                print(vehiculo)

        if opcion == 2:
            print("Buscando los clientes...\n")
            nbast = input("Numero de bastidor(2 int y 1 chr) > ")
            vehiculo = Vehiculos.buscar(nbast=nbast)
            print(vehiculo) if vehiculo else print("Vehiculo no encontrado.")


        # if opcion == 3:


        # if opcion == 4:


        # if opcion == 5:


        # if opcion == 6:


        # if opcion == 7: 
print(iniciar())                    