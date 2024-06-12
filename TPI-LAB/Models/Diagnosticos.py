class Diagnostico:
    def __init__(self,mascota="",diagnostico=""):
        self.mascota = mascota
        self.diagnostico = diagnostico
    
    def __repr__(self):
        return f"El diagnostico de {self.mascota} es {self.diagnostico}"
    
    def setDiagnostico(self,diagNew):
        self.diagnostico = diagNew

    def eliminarDiagnostico(self):
        self.mascota = ""
        self.diagnostico = ""