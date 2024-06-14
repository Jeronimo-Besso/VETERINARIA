from Models.Mascotas import Mascotas
from Views.VistaMascotas import VistaMascotas

class ControllerMascotas:
    def __init__(self):
        self.model = Mascotas()
        self.vista = VistaMascotas()
        self.listaMascotas = []
    def setListaPropietarios(self,lista):
        self.listaPropietarios = lista    
    def setListaRazas(self,lista):
        self.listaRazas = lista
    def getListaMascotas(self):
        return self.listaMascotas
#######################################################################################    
    def buscarObj(self,codigo,new):
        if new == 1: #raza
            for i in self.listaRazas:
                if i.nombre == codigo:
                    return i
        elif new == 2: #prop
            for i in self.listaPropietarios:
                if i.codigo == codigo:
                    return i                
    def cargarLista(self):
        with open("mascotas.txt") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            codigo,nombre,especie,raza,propietario = linea.strip().split(",")
            razaObj = self.buscarObj(raza,1)
            propietarioObj = self.buscarObj(int(propietario),2)
            self.listaMascotas.append(Mascotas(int(codigo),nombre,especie,razaObj,propietarioObj))
#######################################################################################   
    def nuevaMascota(self):
        codigo,nombre,especie,raza,propietario = self.vista.crearNuevaMascota()
        raza = self.buscarObj(raza,1)
        propietario = self.buscarObj(propietario,2)
        self.listaMascotas.append(Mascotas(codigo,nombre,especie,raza,propietario))
    def modificarMascota(self):
        pregunta = self.vista.pregunta()
        for i in self.listaMascotas:
            if i.codigo == pregunta:
                codigo,nombre,especie,raza,propietario = self.vista.crearNuevaMascota()
                razaObj = self.buscarObj(raza,1)
                propietarioObj = self.buscarObj(propietario,2)
                i.setMascota(codigo,nombre,especie,razaObj,propietarioObj)    
    def eliminarMascota(self):
        pregunta = self.vista.pregunta()
        for i in self.listaMascotas:
            if i.codigo == pregunta:
                i.setMascota("","","","","")




                