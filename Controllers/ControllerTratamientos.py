from Views.VistaTratamiento import VistaTratamiento
from Models.Tratamientos import Tratamientos
class ControllerTratamiento:
    def __init__(self):
        self.vista = VistaTratamiento()
        self.model = Tratamientos()
        self.listaTratamientos = []

    def getListaTratamientos(self):
        return self.listaTratamientos

    def buscarObj(self,codigo):
        for i in self.listaMascotas:
            if i.codigo == codigo:
                return i
    
    def cargarTratamientos(self):
        with open("tratamientos.txt") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            codigo,tratamientos = linea.strip().split(",")
            self.listaTratamientos.append(Tratamientos(codigo,tratamientos))
    
    def nuevoTratamiento(self):
        x=0
        codigo,tratamientos = self.vista.nuevoTratamiento()
        for i in self.listaTratamientos:
            if i.codigo == codigo:
                x = 1
                self.vista.aviso(5)
                self.nuevoTratamiento()
        if x==0:
            self.listaTratamientos.append(Tratamientos(codigo,tratamientos))
            self.vista.aviso(1,codigo)
            return codigo

    def modificarTratamientos(self):
        x = 0
        pregunta = self.vista.tratamientoMod(1)
        for i in self.listaTratamientos:
            if i.codigo == pregunta:
                x = 1
                newTratramiento = self.vista.tratamientoNuevo()
                i.set_tratamiento(newTratramiento)
                self.vista.aviso(2,pregunta)
        if x == 0:
            self.vista.aviso(4)
        
    def eliminarTramiento(self):
        x=0
        pregunta = self.vista.tratamientoMod(2)
        for i in self.listaTratamientos:
            x = 1
            if i.codigo == pregunta:
                i.eliminarTratamiento()
                self.vista.aviso(2)
        if x == 0:
            self.vista.aviso(4)
    
    def verLista(self):
        self.vista.verLista(self.listaTratamientos)
    def cargarDatos(self):
        with open("tratamientos.txt","w") as archivo:
            for i in self.listaTratamientos:
                linea = f"{i.codigo},{i.tratamiento}\n"
                archivo.write(linea)
    
    def cantidadTratamientos(self):
        sum = 0
        for i in self.listaTratamientos:
            sum = sum + 1
        self.vista.mostrar(sum)