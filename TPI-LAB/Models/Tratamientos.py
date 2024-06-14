class Tratamientos:
    def __init__(self,mascota="",tratamiento=""):
        self.mascota = mascota
        self.tratamiento = tratamiento
    def set_tratamiento(self,new):
        self.tratamiento = new
    def eliminarTratamiento(self):
        self.mascota = ""
        self.tratamiento = "" 
    def __repr__(self):
        return f"Para la mascota: {self.mascota} el tratamiento es {self.tratamiento}"