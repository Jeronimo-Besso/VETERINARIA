class Consultas:
    def __init__(self,codigo="",fecha="",veterinario="",diagnostico="",tratamiento="",vacunas="",mascota=""):
        self.codigo = codigo
        self.fecha = fecha
        self.veterinario = veterinario
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.vacunas = vacunas
        self.mascota = mascota
    
    def __repr__(self):
        return f"{self.codigo}"



