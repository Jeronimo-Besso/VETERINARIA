from Models.Personas import Personas
class Veterinarios(Personas):
    def __init__(self,codigo="",nombre="",telefono="",especialidad=""):
        super().__init__(codigo,nombre,telefono)
        self.especialidad = especialidad
    
    def modificarPersona(self,codigo,nombre,telefono,especialidad):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono
        self.especialidad = especialidad
    def eliminarPersona(self):
        self.codigo = ""
        self.nombre = ""
        self.telefono = ""
        self.especialidad = ""
    def __repr__(self):
        return f"Veterinario {self.nombre},codigo {self.codigo},su telefono es {self.telefono} y su especialidad es {self.especialidad}"