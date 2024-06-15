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
    def actualizarDatos(self):
        with open("veteriario.txt","w") as archivo:
            for i in self.listaVeterinarios:
                archivo.write(i)
#######################################################################################  
    def crearVeterinario(self):
        codigo,nombre,telefono,especialidad = self.vista.datosVeterinarios()
        self.listaVeterinarios.append(Veterinarios(codigo,nombre,telefono,especialidad))
        with open("veterinario.txt","a") as archivo:
            archivo.write(f"\n{codigo},{nombre},{telefono},{especialidad}")    
    def modificarVeterinario(self):
        vet_modificar = self.vista.pregunta()
        for i in self.listaVeterinarios:
            if i.codigo == vet_modificar:
                codigo,nombre,telefono,especialidad = self.vista.datosVeterinarios()
                i.modificarPersona(codigo,nombre,telefono,especialidad)
                self.vista.aviso()    
    def eliminarVeterinario(self):
        vet = self.vista.pregunta()
        for i in self.listaVeterinarios:
            if i.codigo == vet:
                i.eliminarPersona()
                self.vista.aviso()






 