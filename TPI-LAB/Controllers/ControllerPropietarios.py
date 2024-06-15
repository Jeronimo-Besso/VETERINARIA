from Models.Propietarios import Propietarios
from Views.VistaPropietarios import VistaPropietarios
class ControllerPropietarios:
    def __init__(self):
        self.vista = VistaPropietarios()
        self.model = Propietarios()
        self.listaPropietarios = []
    def getListaProp(self):
        return self.listaPropietarios
#######################################################################################      
    def cargarLista(self):
        with open("propietarios.txt") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            codigo,nombre,telefono = linea.strip().split(",")
            self.listaPropietarios.append(Propietarios(int(codigo),nombre,telefono))   
#######################################################################################   
    def actualizarDatos(self):
        with open("propietarios.txt","w") as archivo:
            for i in self.listaPropietarios:
                archivo.write(i)   
    def crearPropietario(self):
        codigo,nombre,telefono = self.vista.datosPropietaro()
        self.listaPropietarios.append(Propietarios(codigo,nombre,telefono))
        with open("propietarios.txt","a") as archivo:
            archivo.write(f"\n{codigo},{nombre},{telefono}")    
    def modificarPropietario(self):
        propietario_modificar = self.vista.pregunta()
        for i in self.listaPropietarios:
            if i.codigo == propietario_modificar:
                codigo,nombre,telefono = self.vista.datosPropietaro()
                i.modificarPersona(codigo,nombre,telefono)
                self.vista.aviso()    
    def eliminarPropietario(self):
        prop = self.vista.pregunta()
        for i in self.listaPropietarios:
            if i.codigo == prop:
                i.eliminarPersona()
                self.vista.aviso()







    