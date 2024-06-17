class VistaPropietarios:
    def pregunta(self):

        pregunta = int(input("Ingrese el codigo del propietario: "))
        return pregunta
    
    def crearPropietaro(self):
        codigo = int(input("Ingrese el codigo del nuevo propietario: "))
        nombre = input("Ingrese el nombre del nuevo propietario: ")
        telefono = input("Ingrese el telefono del nuevo propietario: ")
        print("Se ha creado el propietario con exito!")
        return codigo,nombre,telefono
    
    def modificarPropietaro(self):
        codigo = int(input("Ingrese el codigo del propietario nuevo: "))
        nombre = input("Ingrese el nombre del propietario nuevo: ")
        telefono = input("Ingrese el telefono del propietario nuevo: ")
        print("Se ha modificado el propietario con exito!")
        return codigo,nombre,telefono
    
    def aviso(self,arg,nombre=""):
        if arg == 1:
            print(f"Propietario {nombre} creado con exito!")
        elif arg ==2:
            print(f"Propietario {nombre} modificado con exito!")
        elif arg ==3:
            print("Propietario eliminado con exito")
        elif arg == 4:
            print("No se ha encontrado el propietario")
        elif arg==5:
            print("Ya existe un propietario con ese codigo!")
    def verLista(self,lista):
        for i in lista:
            print(i)