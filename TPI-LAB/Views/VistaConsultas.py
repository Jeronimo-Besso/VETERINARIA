class VistaConsultas: 
    def crearConsulta(self,arg):
        if arg==1:
            codigo = int(input("Ingrese el codigo de la consulta: "))
            return codigo
        elif arg==2:
            fecha = input("Ingrese la fecha en la que se crea la ficha: ")
            return fecha
        elif arg==3:
            veterinario = int(input("Ingrese el codigo del veterinario asignado: "))
            return veterinario
        elif arg==4:
            diagnostico = int(input("Ingrese el codigo del diagnostico: "))
            return diagnostico
        elif arg==5:
            tratamiento = input("Ingrese el codigo del tratramiento: ")
            return tratamiento
        elif arg==6:
            vacunas = int(input("Ingrese el codigo de la vacuna: "))
            return vacunas
        elif arg==7:
            mascota = int(input("Ingrese el codigo de la mascota: "))
            return mascota    
    def verLista(self,lista):
        for i in lista:
            print(i)