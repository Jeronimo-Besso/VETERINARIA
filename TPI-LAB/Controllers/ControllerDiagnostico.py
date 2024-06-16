from Models.Diagnosticos import Diagnostico
from Views.VistaDiagnostico import VistaDiagnostico

class ControllerDiagnostico:
    def __init__(self):
        self.vista = VistaDiagnostico()
        self.model = Diagnostico()
        self.listaDiagnosticos = []  
    def get_listaDiagnosticos(self):
        return self.listaDiagnosticos
#######################################################################################   
    def cargarLista(self):
        with open ("diagnosticos.txt") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            nro,diagnostico = linea.strip().split(",")
            self.listaDiagnosticos.append(Diagnostico(int(nro),diagnostico))
#######################################################################################    
    def crearDiagnostico(self):
        x=0
        nro,diagnostico = self.vista.diagnosticoNuevo()   
        for i in self.listaDiagnosticos:
            if i.nro == nro:
                x=1
                self.vista.aviso(5)
                self.crearDiagnostico()
        if x == 0:
            self.listaDiagnosticos.append(Diagnostico(nro,diagnostico))
            self.vista.aviso(1,nro)
            return nro
    
    def modificarDiagnostico(self):
        x=0
        pregunta = self.vista.pregunta(2)
        for i in self.listaDiagnosticos:
            if i.nro == pregunta:
                x = 1
                newDiagnostico = self.vista.modificarDiagnostico()
                i.setDiagnostico(newDiagnostico)
                self.vista.aviso(2,pregunta)
        if x == 0:
            self.vista.aviso(4)
                    
    def eliminarDiagnostico(self):
        x = 0
        pregunta = self.vista.pregunta(1)
        for i in self.listaDiagnosticos:
            if i.nro == pregunta:
                x = 1
                i.eliminarDiagnostico()
                self.vista.aviso(3,pregunta)
        if x == 0:
            self.vista.aviso(4)
#######################################################################################
    def verLista(self):
        self.vista.verLista(self.listaDiagnosticos)
    def cargarDatos(self):
        with open("diagnosticos.txt","w") as archivo:
            for i in self.listaDiagnosticos:
                linea = f"{i.nro},{i.diagnostico}\n"
                archivo.write(linea)

        