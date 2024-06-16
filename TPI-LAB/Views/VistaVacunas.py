class VistaVacunas:
    def nuevaVac(self):
        codigo = int(input("Ingrese el codigo de la vacuna nueva: "))
        nombre = input("Ingrese el nombre de la vacuna nueva: ")
        dosis = float(input("Ingrese la dosis de la vacuna nueva: "))
        return codigo,nombre,dosis
    
    def pregunta(self,arg):
        if arg==1:
            pregunta = int(input("Ingrese el codigo de la vacuna a modificar: "))
        if arg==2:
            pregunta = int(input("Ingrese el codigo de la vacuna a eliminar: "))
        return pregunta
    
    def aviso(self,arg,nombre=""):
        if arg==1:
            print(f"Vacuna creada con exito la vacuna {nombre} !")
        elif arg==2:
            print(f"La vacuna {nombre}  ha sido modificada con exito!")
        elif arg==3:
            print("Vacuna eliminada con exito!")
        elif arg==4:
            print("No se encontro la vacuna")
        elif arg==5:
            print("La vacuna ya existe!")
    def verLista(self,lista):
        for i in lista:
            print(i)