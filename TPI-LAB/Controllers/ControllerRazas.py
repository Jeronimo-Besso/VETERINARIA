from Models.Razas import Razas
from Views.VistaRaza import VistaRaza

class ControllerRazas:
    def __init__(self):
        self.vista = VistaRaza()
        self.model = Razas()
        self.listaRazas = []
    def getListaRaza(self):
        return self.listaRazas
    def actualizarDatos(self):
        with open("razas.txt","w") as archivo:
            for i in self.listaRazas:
                archivo.write(i)           
    
    def cargarLista(self):
        with open("razas.txt") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            nombre,caracteristicas = linea.strip().split(",")
            self.listaRazas.append(Razas(nombre,caracteristicas))
    
    def crearRaza(self):
        nombre,caracteristica = self.vista.crearRaza()
        self.listaRazas.append(Razas(nombre,caracteristica))
        with open("razas.txt","a") as archivo:
            archivo.write(f"\n{nombre},{caracteristica}")
    
    def modificarRaza(self):
        razaCambio = self.vista.pregunta()
        for i in self.listaRazas:
            if i.nombre == razaCambio:
                nombre,caracteristicas = self.vista.crearRaza()
                i.setRaza(nombre,caracteristicas)
                self.vista.aviso()
    
    def eliminarRaza(self):
        raza = self.vista.raza_eliminar()
        for i in self.listaRazas:
            if i.nombre == raza:
                i.eliminarRaza()
                self.vista.aviso()
        