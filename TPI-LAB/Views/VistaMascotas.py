class VistaMascotas:
    def crearNuevaMascota(self):
        codigo = int(input("Ingrese el codigo de la mascota: "))
        nombre = input("Ingrese el nombre de la mascota: ")
        especie = input("Ingrese el nombre de la especie: ")
        raza = input("Ingrese el nombre de la raza: ")
        propietario = int(input("Ingrese el codigo del propietario: "))
        return codigo,nombre,especie,raza,propietario
    def pregunta(self):
        preg = int(input("Ingrese el codigo de la mascota: "))
        return preg