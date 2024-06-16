from Models.Veterinarios import Veterinarios
from Views.VistaVeterinarios import VistaVeterinarios

class ControllerVeterinarios:
    def __init__(self):
        self.vista = VistaVeterinarios()
        self.model = Veterinarios()
        self.listaVeterinarios = []
#######################################################################################      
    def cargarLista(self):
        with open("veterinario.txt") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            codigo,nombre,telefono,especialidad = linea.strip().split(",")
            self.listaVeterinarios.append(Veterinarios(int(codigo),nombre,telefono,especialidad))
    def getListaVeterinarios(self):
        return self.listaVeterinarios
#######################################################################################      
#######################################################################################  
    def crearVeterinario(self):
        x=0
        codigo,nombre,telefono,especialidad = self.vista.datosVeterinarios()
        for i in self.listaVeterinarios:
            if i.codigo == codigo:
                x=1
                self.vista.aviso(5)
                self.crearVeterinario()
        if x==0:
            self.listaVeterinarios.append(Veterinarios(codigo,nombre,telefono,especialidad))
            self.vista.aviso(1,nombre)
            return codigo
    
    def modificarVeterinario(self):
        x=0
        vet_modificar = self.vista.pregunta()
        for i in self.listaVeterinarios:
            if i.codigo == vet_modificar:
                x=1
                codigo,nombre,telefono,especialidad = self.vista.datosVeterinarios()
                i.modificarPersona(codigo,nombre,telefono,especialidad)
                self.vista.aviso(2,nombre)    
        if x==0:
            self.vista.aviso(4)
    
    def eliminarVeterinario(self):
        x=0
        vet = self.vista.pregunta()
        for i in self.listaVeterinarios:
            if i.codigo == vet:
                x=1
                i.eliminarPersona()
                self.vista.aviso(3)
        if x==0:
            self.vista.aviso(4)
    def verLista(self):
        self.vista.verLista(self.listaVeterinarios)

    def cargarDatos(self):
        with open("veterinario.txt","w") as archivo:
            for i in self.listaVeterinarios:
                linea = f"{i.codigo},{i.nombre},{i.telefono},{i.especialidad}\n"
                archivo.write(linea)
    


 