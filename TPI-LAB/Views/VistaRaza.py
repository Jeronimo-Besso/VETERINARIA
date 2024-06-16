class VistaRaza:
    def crearRaza(self):
        nombre = input("Ingrese el nombre de la raza nueva: ")
        if nombre != "" and type(nombre) != int and type(nombre) != float:
            caracteristicas = input(f"Ingrese las caracteristicas de la raza {nombre}: ")
            return nombre,caracteristicas

    def pregunta(self):
        rta = input("Que raza desea modificar? Ingrese el nombre: ")
        return rta
    
    
    def raza_eliminar(self):
        nombre= input("Ingrese el nombre de la raza que desea eliminar: ")
        return nombre
    
    def aviso(self,arg,nombre = ""):
        if arg == 1:
            print("Raza eliminada con exito")
        elif arg ==2:
            print("No se ha encontrado la raza")
        elif arg ==3:
            print(f"Raza {nombre} creada con exito")
        elif arg == 4:
            print(f"Raza {nombre} modificada con exito")
        elif arg==5:
            print("La raza ya existe!")
    def verLista(self,lista):
        for i in lista:
            print(i)
        