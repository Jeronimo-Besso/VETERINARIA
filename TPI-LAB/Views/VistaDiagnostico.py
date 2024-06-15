class VistaDiagnostico:
    def pregunta(self):
        pregunta = int(input("Ingrese el numero del diagnostico: "))
        return pregunta
    
    def diagnosticoNuevo(self):
        nro = int(input("Ingrese el numero de diagnostico nuevo: "))
        mascota = int(input("Ingrese el codigo de la mascota a la que se le hara el diagnostico:"))
        diagnostico = input("Ingrese el diagnostico: ")
        return nro,mascota,diagnostico
    
    def modificarDiagnostico(self):
        diagnostico = input("Cree el nuevo diagnostico: ")
        return diagnostico