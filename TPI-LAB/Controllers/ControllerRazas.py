from Models.Razas import Razas
from Views.VistaRaza import VistaRaza

class ControllerRazas:
    def __init__(self):
        self.vista = VistaRaza()
        self.model = Razas()
        self.listaRazas = []
    
    def getListaRaza(self):
        return self.listaRazas
#######################################################################################  
#######################################################################################      
    def cargarLista(self):
        with open("razas.txt") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            nombre,caracteristicas = linea.strip().split(",")
            self.listaRazas.append(Razas(nombre,caracteristicas))
#######################################################################################      
    def crearRaza(self):
        x=0
        nombre,caracteristica = self.vista.crearRaza()
        for i in self.listaRazas:
            if i.nombre == nombre:
                x = 1
                self.aviso(5)
        if x==0:
            self.listaRazas.append(Razas(nombre,caracteristica))
            self.vista.aviso(3,nombre)
            return nombre 
    def modificarRaza(self):
        x = 0
        razaCambio = self.vista.pregunta()
        for i in self.listaRazas:
            if i.nombre == razaCambio:
                x = 1
                nombre,caracteristicas = self.vista.crearRaza()
                i.setRaza(nombre,caracteristicas)
                self.vista.aviso(4,nombre)
        if x == 0:
            self.vista.aviso(2)   
    def eliminarRaza(self):
        x= 0
        raza = self.vista.raza_eliminar()
        for i in self.listaRazas:
            if i.nombre == raza:
                x = 1
                i.eliminarRaza()
                self.vista.aviso(1)
        if x == 0:
            self.vista.aviso(2)     
    def verLista(self):
        self.vista.verLista(self.listaRazas)
    def cargarDatos(self):
        with open("razas.txt","w") as archivo:
            for i in self.listaRazas:
                linea = f"{i.nombre},{i.caracteristicas}\n"
                archivo.write(linea)
    



