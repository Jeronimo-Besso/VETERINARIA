class VistaDiagnostico:
    def pregunta(self,arg):
        if arg== 1:
            pregunta = int(input("Ingrese el numero del diagnostico a eliminar: "))
        elif arg ==2:
            pregunta = int(input("Ingrese el numero del diagnostico a modificar: "))
        return pregunta
    
    def diagnosticoNuevo(self):
        nro = int(input("Ingrese el numero de diagnostico nuevo: "))
        diagnostico = input("Ingrese el diagnostico: ")
        return nro,diagnostico
    
    def modificarDiagnostico(self):
        diagnostico = input("Cree el nuevo diagnostico: ")
        print("El diagnostico se ha modificado!")
        return diagnostico
    

    def aviso(self,arg,arg2=0):
        if arg == 1:
            print(f"Se ha creado el diagnostico nro {arg2}")
        elif arg == 2:
            print(f"Se ha modificado el diagnostico nro{arg2}")
        elif arg ==3:
            print(f"Se ha eliminado el diagnostico nro {arg2}")
        elif arg == 4:
            print("No se ha encontrado el diagnostico")
        elif arg==5:
            print("El nro ya existe!")
    def verLista(self,lista):
        for i in lista:
            print(i)

