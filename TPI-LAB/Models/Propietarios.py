from Models.Personas import Personas
class Propietarios(Personas):
    def __init__(self,codigo="",nombre="",telefono=""):
        super().__init__(codigo,nombre,telefono)
