class VistaTratamiento: 
    def tratamientoMod(self,arg):
        if arg ==1:
            tratamiento = input("Ingrese el codigo del tratamiento que desea modificar: ")
        elif arg == 2:
            tratamiento = input("Ingrese el codigo del tratamiento que desea eliminar: ")
        return tratamiento
    
    def nuevoTratamiento(self):
        codigo = input("Ingrese el codigo del tratamiento nuevo : ")
        tratamiento = input("Ingrese el tratamiento nuevo: ")
        return codigo,tratamiento
    
    def tratamientoNuevo(self):
        newTratamiento = input("Ingrese el tratamiento nuevo: ")
        return newTratamiento
     
    def aviso(self,arg,codigo=""):
        if arg == 1:
            print(f"Se ha creado el tratamiento {codigo} con exito")
        elif arg ==2:
            print(f"Se ha modificado el tratamiento {codigo} con exito")
        elif arg == 3:
            print("Se ha eliminado el tratamiento")
        elif arg ==4:
            print("El tratamiento no se encontro!")
        elif arg==5:
            print("El tratamiento ya existe!")
    def verLista(self,lista):
        for i in lista:
            print(i)
    def mostrar(self,sum):
        print(f"La cantidad de tratamientos hechos por esta veterianaria es de {sum}")