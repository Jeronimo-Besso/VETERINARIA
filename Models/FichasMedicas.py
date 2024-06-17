class FichasMedicas:
    def __init__(self,codigo="",consultas="",mascota=""):
        self.codigo = codigo
        self.consultas = consultas
        self.mascota = mascota

    def crearFicha(self,codigo,consultasNew,mascotaNew):
        self.codigo = codigo
        self.consultas = consultasNew
        self.mascota = mascotaNew

    def __repr__(self):
        return f"Ficha medica: {self.codigo}, {self.consultas}. FICHA MEDICA DE LA MASCOTA {self.mascota}"