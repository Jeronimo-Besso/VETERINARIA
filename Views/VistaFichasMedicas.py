class VistaFichasMedicas:
    def crearFicha(self):
        codigo = int(input("Ingrese el codigo de la ficha nueva: "))
        consultas = input("Ingrese el codigo de las consultas para la ficha nueva ( si es mas de uno separar por ; ): ")
        return codigo,consultas
    def buscarFicha(self):
        mascota = int(input("Ingrese codigo de mascota a buscar: "))
        return mascota
    def verLista(self,lista):
        for i in lista:
            print(i)