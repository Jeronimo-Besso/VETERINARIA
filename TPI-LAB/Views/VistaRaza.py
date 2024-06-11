class VistaRaza:
    def crearRaza(self):
        nombre = input("Ingrese el nombre de la raza: ")
        caracteristicas = input("Ingrese las caracteristicas de la raza: ")
        return nombre,caracteristicas
    def pregunta(self):
        rta = input("Que raza desea cambiar? Ingrese el nombre: ")
        return rta
    def raza_eliminar(self):
        nombre= input("Ingrese el nombre de la raza que desea eliminar: ")
        return nombre
    def aviso(self):
        print("No te olvides actualizar los datos antes de cerrar el programa!")