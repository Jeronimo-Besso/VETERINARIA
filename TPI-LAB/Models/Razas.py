class Razas:
    def __init__(self,nombre="",caracteristicas=""):
        self.nombre = nombre
        self.caracteristicas = caracteristicas
    def setRaza(self,nombreNew,caracNew):
        self.nombre = nombreNew
        self.caracteristicas = caracNew
    def eliminarRaza(self):
        self.nombre = ""
        self.caracteristicas = ""
    def __repr__(self):
        return f"{self.nombre}"
