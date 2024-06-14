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
    def modificarTratamientos(self):
        pregunta = self.vista.pregunta()
        for i in self.listaTratamientos:
            if i.mascota.codigo == pregunta:
                newTratramiento = self.vista.preguntaTrat()
                i.set_tratamiento(newTratramiento)
                self.vista.aviso(1)
    def eliminarTramiento(self):
        pregunta = self.vista.pregunta()
        for i in self.listaTratamientos:
            if i.mascota.codigo == pregunta:
                i.eliminarTratamiento()
                self.vista.aviso(2)


    