from Models.Diagnosticos import Diagnostico
from Views.VistaDiagnostico import VistaDiagnostico

class ControllerDiagnostico:
    def __init__(self):
        self.vista = VistaDiagnostico()
        self.model = Diagnostico()
        self.listaDiagnosticos = []
    
    def setListaMascotas(self,lista):
        self.listaMascotas = lista
    
    def buscarObj(self,codigo):
        for i in self.listaMascotas:
            if i.codigo == codigo:
                return i

    def cargarLista(self):
        with open ("diagnosticos.txt") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            mascota,diagnostico = linea.strip().split(",")
            mascota = self.buscarObj(int(mascota))
            self.listaDiagnosticos.append(Diagnostico(mascota,diagnostico))
    
    def crearDiagnostico(self):
        pregunta = self.vista.pregunta()
        for i in self.listaDiagnosticos:
            if i.mascota.codigo == pregunta:
                diagnostico = self.vista.diagnosticoNuevo()
                mascota = self.buscarObj(pregunta)
                self.listaDiagnosticos.append(Diagnostico(mascota,diagnostico))
                break
    
    def modificarDiagnostico(self):
        pregunta = self.vista.pregunta()
        for i in self.listaDiagnosticos:
            if i.mascota.codigo == pregunta:
                newDiagnostico = self.vista.diagnosticoNuevo()
                i.setDiagnostico(newDiagnostico)
    
    def eliminarDiagnostico(self):
        pregunta = self.vista.pregunta()
        for i in self.listaDiagnosticos:
            if i.mascota.codigo == pregunta:
                i.eliminarDiagnostico()


        