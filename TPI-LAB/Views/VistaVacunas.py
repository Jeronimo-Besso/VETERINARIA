class VistaVacunas:
    def nuevaVac(self):
        codigo = int(input("Ingrese el codigo de la vacuna: "))
        nombre = input("Ingrese el nombre de la vacuna: ")
        dosis = float(input("Ingrese la dosis de la vacuna: "))
        return codigo,nombre,dosis
    
    def pregunta(self):
        pregunta = int(input("Ingrese el codigo de la vacuna a editar/crear/eliminar: "))
        return pregunta
    
    def aviso(self):
        print("Accion realizada con exito")