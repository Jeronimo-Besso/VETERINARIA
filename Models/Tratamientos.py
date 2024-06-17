class Tratamientos:
    def __init__(self,codigo="",tratamiento=""):
        self.codigo = codigo
        self.tratamiento = tratamiento
    
    def set_tratamiento(self,new):
        self.tratamiento = new
    
    def eliminarTratamiento(self):
        self.codigo = ""
        self.tratamiento = "" 
    
    
    def __repr__(self):
        return f"Tratamiento codigo {self.codigo},es {self.tratamiento}"