class Diagnostico:
    def __init__(self,nro="",mascota="",diagnostico=""):
        self.nro = nro
        self.mascota = mascota
        self.diagnostico = diagnostico
    
    def __repr__(self):
        return f"el diagnostico es {self.diagnostico}"
    
    def setDiagnostico(self,diagNew):
        self.diagnostico = diagNew

    def eliminarDiagnostico(self):
        self.nro = ""
        self.mascota = ""
        self.diagnostico = ""