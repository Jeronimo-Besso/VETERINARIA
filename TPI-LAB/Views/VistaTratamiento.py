class VistaTratamiento: 
    def pregunta(self):
        mascota = int(input("Ingrese el codigo de la mascota que desea: "))
        return mascota
    
    def nuevoTratamiento(self):
        codigo = input("Ingrese el codigo del tratamiento: ")
        mascota = int(input("Ingrese el codigo de la mascota a la que le quiere asignar un nuevo tratamiento: "))
        tratamiento = input("Ingrese el tratamiento: ")
        return codigo,mascota,tratamiento
    
    def preguntaTrat(self):
        newTratamiento = input("Ingrese el tratamiento: ")
        return newTratamiento
     
    def aviso(self,arg):
        if arg == 1:
            print("Se ha modificado el tratamiento con exito")
        elif arg == 2:
            print("Se ha eliminado el tratamiento")