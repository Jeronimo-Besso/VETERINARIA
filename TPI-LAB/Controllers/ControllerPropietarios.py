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
    def crearPropietario(self):
        x=0
        codigo,nombre,telefono = self.vista.crearPropietaro()
        for i in self.listaPropietarios:
            if i.codigo == codigo:
                x = 1
                self.aviso(5)
                self.crearPropietario()
        if x ==0:
            self.listaPropietarios.append(Propietarios(codigo,nombre,telefono))  
            self.vista.aviso(1,nombre)
            return codigo
    
    def modificarPropietario(self):
        x = 0
        propietario_modificar = self.vista.pregunta()
        for i in self.listaPropietarios:
            if i.codigo == propietario_modificar:
                x = 1
                codigo,nombre,telefono = self.vista.modificarPropietaro()
                i.modificarPersona(codigo,nombre,telefono)
                self.vista.aviso(2,nombre)
        if x == 0:
            self.vista.aviso(4)
    
    def eliminarPropietario(self):
        x=0
        prop = self.vista.pregunta()
        for i in self.listaPropietarios:
            if i.codigo == prop:
                x = 1
                i.eliminarPersona()
                self.vista.aviso(3)
        if x == 0:
            self.vista.aviso(4)
    def verLista(self):
        self.vista.verLista(self.listaPropietarios)
    def cargarDatos(self):
        with open("propietarios.txt","w") as archivo:
            for i in self.listaPropietarios:
                linea = f"{i.codigo},{i.nombre},{i.telefono}\n"
                archivo.write(linea)






    