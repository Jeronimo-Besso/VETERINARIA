class Mascotas:
    def __init__(self,codigo="",nombre="",especie="",raza="",propietario=""):
        self.codigo = codigo
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.propietario = propietario
    
    def setMascota(self,codigo,nombre,especie,raza,propietario):
        self.codigo = codigo
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.propietario = propietario
    
    def __repr__(self):
        return f"{self.codigo}"