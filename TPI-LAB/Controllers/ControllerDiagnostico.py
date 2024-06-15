from Models.Diagnosticos import Diagnostico
from Views.VistaDiagnostico import VistaDiagnostico

class ControllerDiagnostico:
    def __init__(self):
        self.vista = VistaDiagnostico()
        self.model = Diagnostico()
        self.listaDiagnosticos = []  
    def setListaMascotas(self,lista):
        self.listaMascotas = lista
    def get_listaDiagnosticos(self):
        return self.listaDiagnosticos
#######################################################################################   
    def buscarObj(self,codigo):
        for i in self.listaMascotas:
            if i.codigo == codigo:
                return i
    def cargarLista(self):
        with open ("diagnosticos.txt") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            nro,mascota,diagnostico = linea.strip().split(",")
            mascota = self.buscarObj(int(mascota))
            self.listaDiagnosticos.append(Diagnostico(int(nro),mascota,diagnostico))
#######################################################################################    
    def crearDiagnostico(self):
        nro,mascota,diagnostico = self.vista.diagnosticoNuevo()   
        mascotaObj = self.buscarObj(mascota)
        self.listaDiagnosticos.append(Diagnostico(nro,mascotaObj,diagnostico))
    
    def modificarDiagnostico(self):
        pregunta = self.vista.pregunta()
        for i in self.listaDiagnosticos:
            if i.nro == pregunta:
                newDiagnostico = self.vista.modificarDiagnostico()
                i.setDiagnostico(newDiagnostico)
                    
    def eliminarDiagnostico(self):
        pregunta = self.vista.pregunta()
        for i in self.listaDiagnosticos:
            if i.mascota.codigo == pregunta:
                i.eliminarDiagnostico()
#######################################################################################


        