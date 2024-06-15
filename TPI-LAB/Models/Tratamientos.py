class Tratamientos:
    def __init__(self,codigo="",mascota="",tratamiento=""):
        self.codigo = codigo
        self.mascota = mascota
        self.tratamiento = tratamiento
    def set_tratamiento(self,new):
        self.tratamiento = new
    def eliminarTratamiento(self):
        self.codigo = ""
        self.mascota = ""
        self.tratamiento = "" 
    
    
    def __repr__(self):
        return f"el tratamiento es {self.tratamiento}"