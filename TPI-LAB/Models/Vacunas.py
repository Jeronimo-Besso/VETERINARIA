class Vacunas:
    def __init__(self,codigo="",nombre="",dosis=""):
        self.codigo = codigo
        self.nombre = nombre
        self.dosis = dosis
    def mod_Vacuna(self,newCodigo,newNombre,newDosis):
        self.codigo = newCodigo
        self.nombre = newNombre
        self.dosis = newDosis
        
    
    def __repr__(self):
        return f"se aplico vacuna {self.nombre}, dosis utilizada: {self.dosis}"