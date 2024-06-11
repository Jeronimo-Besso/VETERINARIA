class Personas:
    def __init__(self,codigo="",nombre="",telefono=""):
        self.nombre = nombre
        self.telefono = telefono
        self.codigo = codigo
    def modificarPersona(self,codigo,nombre,telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono
    def eliminarPersona(self):
        self.codigo = ""
        self.nombre = ""
        self.telefono = ""
    def __repr__(self):
        return f"Nombre: {self.nombre} telefono: {self.telefono}"