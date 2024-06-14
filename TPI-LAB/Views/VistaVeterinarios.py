class VistaVeterinarios:
    def datosVeterinarios(self):
        codigo = int(input("Ingrese el codigo del veterinario: "))
        nombre = input("Ingrese el nombre del veterinario: ")
        telefono = input("Ingrese el telefono del veterinario: ")
        especialidad = input("Ingrese la especialidad del veterinario: ")
        return codigo,nombre,telefono,especialidad
    def pregunta(self):
        codigo = int(input("Ingrese el codigo del veterinario: "))
        return codigo
    def aviso(self):
        print("No te olvides actualizar los datos antes de cerrar el programa!")