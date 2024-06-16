from Models.FichasMedicas import FichasMedicas
from Views.VistaFichasMedicas import VistaFichasMedicas

class ControllerFichasMedicas:
    def __init__(self):
        self.vista = VistaFichasMedicas()
        self.model = FichasMedicas()
        self.listaFichas = []

    def cargarListas(self,listaMascotas,listaConsultas):
        self.listaMascotas = listaMascotas
        self.listaConsultas = listaConsultas

    def crearFichas(self):
        codigo = 1
        for i in self.listaMascotas:
            listaConsultas = []
            for j in self.listaConsultas:
                if j.mascota.codigo == i.codigo:
                    listaConsultas.append(j)
            self.listaFichas.append(FichasMedicas(codigo,listaConsultas))
            codigo = codigo + 1
    def verLista(self):
        self.vista.verLista(self.listaFichas)
    def cargarDatos(self):
        with open("fichasMedicas.txt","w") as archivo:
            for i in self.listaFichas:
                linea = f"{i.codigo},{i.consultas},{i.mascota}\n"
                archivo.write(linea)
