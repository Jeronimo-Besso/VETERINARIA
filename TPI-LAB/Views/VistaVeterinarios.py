class VistaVeterinarios:
    def datosVeterinarios(self):
        codigo = int(input("Ingrese el codigo del veterinario: "))
        nombre = input("Ingrese el nombre del veterinario: ")
        telefono = input("Ingrese el telefono del veterinario: ")
        especialidad = input("Ingrese la especialidad del veterinario: ")
        return codigo,nombre,telefono,especialidad
    
    def pregunta(self,arg):
        if arg==1:
            codigo = int(input("Ingrese el codigo del veterinario que desea modificar: "))
        elif arg==2:
            codigo = int(input("Ingrese el codigo del veterinario que desea eliminar: "))
        return codigo
    
    def aviso(self,arg,nombre=""):
        if arg==1:
            print(f"El veterinario/a {nombre}  se ha cargado con exito!")
        elif arg==2:
            print(f"El veterinario/a {nombre}  ha sido modificada con exito!")
        elif arg==3:
            print("Veterinario/a eliminada/o con exito!")
        elif arg==4:
            print("No se encontro el/la veterinario/a")
        elif arg==5:
            print("Ya existe el codigo de veterinario!")
    def verLista(self,lista):
        for i in lista:
            print(i)