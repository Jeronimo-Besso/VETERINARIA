from Models.Personas import Personas
class Propietarios(Personas):
    def __init__(self,codigo="",nombre="",telefono=""):
        super().__init__(codigo,nombre,telefono)
    
    def __repr__(self):
        return f"Nombre del propietario {self.nombre}, numero de telefono {self.telefono}, codigo {self.codigo}"