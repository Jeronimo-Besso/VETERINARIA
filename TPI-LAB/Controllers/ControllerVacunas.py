from Models.Vacunas import Vacunas
from Views.VistaVacunas import VistaVacunas

class ControllerVacunas:
    def __init__(self):
        self.vista = VistaVacunas()
        self.model = Vacunas()
        self.listaVacunas = []
    
    def getListaVacunas(self):
        return self.listaVacunas

    def cargarVacunas(self):
        with open("vacunas.txt") as archivo:
            lineas = archivo.readlines()
        for i in lineas:
            codigo,nombre,dosis = i.strip().split(",")
            self.listaVacunas.append(Vacunas(int(codigo),nombre,float(dosis)))
    
    def nuevaVacuna(self):
        codigo,nombre,dosis = self.vista.nuevaVac()
        self.listaVacunas.append(Vacunas(codigo,nombre,dosis))
        self.vista.aviso()
    
    def modificarVacuna(self):
        pregunta = self.vista.pregunta()
        for i in self.listaVacunas:
            if i.codigo == pregunta:
                codigo,nombre,dosis = self.vista.nuevaVac()
                i.mod_Vacuna(codigo,nombre,dosis)
                self.vista.aviso()
    
    def eliminarVacunas(self):
        pregunta = self.vista.pregunta()
        for i in self.listaVacunas:
            if i.codigo == pregunta:
                i.mod_Vacuna("","","")