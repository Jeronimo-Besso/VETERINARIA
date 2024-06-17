class VistaMascotas:
    def crearNuevaMascota(self):
        codigo = int(input("Ingrese el codigo de la nueva mascota: "))
        nombre = input("Ingrese el nombre de la nueva mascota: ")
        especie = input("Ingrese el nombre de la especie: ")
        raza = input("Ingrese el nombre de la raza: ")
        propietario = int(input("Ingrese el codigo del propietario: "))
        return codigo,nombre,especie,raza,propietario
    
    def modificarMascota(self):
        codigo = int(input("Ingrese el codigo de la mascota: "))
        nombre = input("Ingrese el nombre de la mascota: ")
        especie = input("Ingrese el nombre de la especie: ")
        raza = input("Ingrese el nombre de la raza: ")
        propietario = int(input("Ingrese el codigo del propietario: "))
        return codigo,nombre,especie,raza,propietario

    def mostrarLista(self,lista):
        for i in lista:
            print(i)
    def pregunta(self):
        preg = int(input("Ingrese el codigo de la mascota: "))
        return preg
    
    def aviso(self,arg1,nombre=""):
        if arg1 == 1:
            print(f"Se ha creado la mascota {nombre}")
        elif arg1 == 2:
            print(f"Se ha modificado la mascota {nombre}")
        elif arg1 == 3:
            print("Se ha eliminado la mascota")
        elif arg1 == 4:
            print("No se ha encontrado la mascota!")
        elif arg1 ==5:
            print("El codigo ya existe en otra mascota!")
        elif arg1 == 6:
            print("No se ha encontrado propietario")
        elif arg1==7:
            print("No se ha encontrado esa raza")
    def verLista(self,lista):
        for i in lista:
            print(i)


