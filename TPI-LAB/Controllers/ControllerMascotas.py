from Models.Mascotas import Mascotas
from Views.VistaMascotas import VistaMascotas

class ControllerMascotas:
    def __init__(self):
        self.model = Mascotas()
        self.vista = VistaMascotas()
        self.listaMascotas = []
    def setListas(self,controladorPropietarios,controladorRazas,propietarios,razas):
        self.controladorPropietarios = controladorPropietarios
        self.controladorRazas = controladorRazas
        self.listaPropietarios = propietarios   
        self.listaRazas = razas
    def getListaMascotas(self):
        return self.listaMascotas
#######################################################################################    
    def buscarObj(self,codigo,new):
        if new == 1: #raza
            a = 0
            for i in self.listaRazas:
                if i.nombre == codigo:
                    a=1
                    return i
            if a==0:
                self.vista.aviso(7)
                nombre = self.controladorRazas.crearRaza()
                for i in self.listaRazas:
                    if i.nombre == nombre:
                        return i 
        elif new == 2: #prop
            b = 0
            for i in self.listaPropietarios:
                if i.codigo == codigo:
                    b=1
                    return i               
            if b==0:
                self.vista.aviso(6)
                codigo = self.controladorPropietarios.crearPropietario()
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
        x=0
        codigo,nombre,especie,raza,propietario = self.vista.crearNuevaMascota()
        razaObj = self.buscarObj(raza,1)
        propietarioObj = self.buscarObj(propietario,2)
        for i in self.listaMascotas:
            if i.codigo == codigo:
                self.vista.aviso(5)
                x = 1
                self.nuevaMascota()
        if x ==0:
            self.listaMascotas.append(Mascotas(codigo,nombre,especie,razaObj,propietarioObj))
            self.vista.aviso(1,nombre)
            return codigo

    
    def modificarMascota(self):
        x = 0
        pregunta = self.vista.pregunta()
        for i in self.listaMascotas:
            if i.codigo == pregunta:
                x = 1
                codigo,nombre,especie,raza,propietario = self.vista.modificarMascota()
                razaObj = self.buscarObj(raza,1)
                propietarioObj = self.buscarObj(propietario,2)
                i.setMascota(codigo,nombre,especie,razaObj,propietarioObj)    
                self.vista.aviso(2,nombre)
        if x == 0:
            self.vista.aviso(4)
    
    def eliminarMascota(self):
        x = 0
        pregunta = self.vista.pregunta()
        for i in self.listaMascotas:
            x = 1
            if i.codigo == pregunta:
                i.setMascota("","","","","")
                self.vista.aviso(3)
        if x == 0:
            self.vista.aviso(4)
    
    def verLista(self):
        self.vista.verLista(self.listaMascotas)
    
    def cargarDatos(self):
        with open("mascotas.txt","w") as archivo:
            for i in self.listaMascotas:
                linea = f"{i.codigo},{i.nombre},{i.especie},{i.raza},{i.propietario}\n"
                archivo.write(linea)

    def contarCant(self):
        listaPropMasc = []
        for i in self.listaPropietarios:
            sum = 0
            for j in self.listaMascotas:
                if i.codigo == j.propietario.codigo:
                    sum = sum + 1
            propObj = self.buscarObj(i.codigo,2)
            listaPropMasc.append((propObj.nombre,sum))
        self.vista.mostrarLista(listaPropMasc)