from Views.VistaTratamiento import VistaTratamiento
from Models.Tratamientos import Tratamientos
class ControllerTratamiento:
    def __init__(self):
        self.vista = VistaTratamiento()
        self.model = Tratamientos()
        self.listaTratamientos = []
    
    def setListaMascotas(self,lista):
        self.listaMascotas = lista

    def buscarObj(self,codigo):
        for i in self.listaMascotas:
            if i.codigo == codigo:
                return i
    
    def cargarTratamientos(self):
        with open("tratamientos.txt") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            mascota,tratamientos = linea.strip().split(",")
            mascota = self.buscarObj(int(mascota))
            self.listaTratamientos.append(Tratamientos(mascota,tratamientos))