class VistaPropietarios:
    def pregunta(self):
        pregunta = int(input("Ingrese el codigo del propietario: "))
        return pregunta
    def datosPropietaro(self):
        codigo = int(input("Ingrese el codigo del propietario: "))
        nombre = input("Ingrese el nombre del propietario: ")
        telefono = input("Ingrese el telefono del propietario: ")
        return codigo,nombre,telefono
    def aviso(self):
        print("No te olvides actualizar los datos antes de cerrar el programa!")