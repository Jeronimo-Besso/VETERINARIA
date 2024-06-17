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
        x=0
        codigo,nombre,dosis = self.vista.nuevaVac()
        for i in self.listaVacunas:
            if i.codigo == codigo:
                x = 1
                self.vista.aviso(5)
                self.nuevaVacuna()
        if x==0:
            self.listaVacunas.append(Vacunas(codigo,nombre,dosis))
            self.vista.aviso(1,nombre)
            return codigo
    
    def modificarVacuna(self):
        x = 0
        pregunta = self.vista.pregunta(1)
        for i in self.listaVacunas:
            if i.codigo == pregunta:
                x=1
                codigo,nombre,dosis = self.vista.nuevaVac()
                i.mod_Vacuna(codigo,nombre,dosis)
                self.vista.aviso(2,nombre)
        if x == 0:
            self.vista.aviso(4)
    
    def eliminarVacunas(self):
        x=0
        pregunta = self.vista.pregunta(2)
        for i in self.listaVacunas:
            if i.codigo == pregunta:
                x=1
                i.mod_Vacuna("","","")
                self.vista.aviso(3)
        if x == 0:
            self.vista.aviso(4)
    def verLista(self):
        self.vista.verLista(self.listaVacunas)
    def cargarDatos(self):
        with open("vacunas.txt","w") as archivo:
            for i in self.listaVacunas:
                linea = f"{i.codigo},{i.nombre},{i.dosis}\n"
                archivo.write(linea)
    


        