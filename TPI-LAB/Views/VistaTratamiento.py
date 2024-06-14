class VistaTratamiento: 
    def pregunta(self):
        mascota = int(input("Ingrese el codigo de la mascota que desea: "))
        return mascota
    def preguntaTrat(self):
        newTratamiento = input("Ingrese el tratamiento: ")
        return newTratamiento
    def aviso(self,arg):
        if arg == 1:
            print("Se ha modificado el tratamiento con exito")
        elif arg == 2:
            print("Se ha eliminado el tratamiento")